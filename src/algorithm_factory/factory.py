import logging
from pathlib import Path

import numpy as np
import onnx
import torch
import torchvision
from PIL import Image
from torchvision.models.detection.faster_rcnn import (
    FasterRCNN_MobileNet_V3_Large_FPN_Weights, FastRCNNPredictor)


class ObjectDetector():
    def __init__(self, project_name, image, model_directory="/model/setup") -> None:
        self.model_path = Path(f"{model_directory}/{project_name}.pt")
        if not self.model_path.exists():
            model = torchvision.models.detection.fasterrcnn_mobilenet_v3_large_fpn(weights=FasterRCNN_MobileNet_V3_Large_FPN_Weights.DEFAULT)
            in_features = model.roi_heads.box_predictor.cls_score.in_features

            # 2 class model
            model.roi_heads.box_predictor = FastRCNNPredictor(in_features, 2)
            torch.save(model, self.model_path)

        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

        self.detection_model = torch.load(self.model_path, map_location=torch.device('cpu')).to(self.device)
        self.detection_model.to(self.device)
        self.detection_model.eval()

        export_output = torch.onnx.export(self.detection_model, image, f"{model_directory}/{project_name}.onnx")

    
    def make_prediction(self, image):
        image = Image.open(image)
        image = image.convert('RGB')
        convert_to_tensor = torchvision.transforms.ToTensor()
        image = convert_to_tensor(image)

        # Perform inference
        try:
            with torch.no_grad():
                preds = self.detection_model([image])[0]

                labels = preds["labels"].cpu().detach().numpy()
                scores = preds["scores"].cpu().detach().numpy()
                boxes = preds["boxes"].cpu().detach().numpy()
                detections = []

                for _, score, box in zip(labels, scores, boxes):
                    if score > 0.5:
                        detections.append(box)
            del image
            return True, np.array(detections)             
        except Exception as e:
            return False, f"Error with predictions: {e}"