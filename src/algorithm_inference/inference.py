import datetime
import logging
from pathlib import Path

import numpy as np
import onnx
import onnxruntime as rt
import torchvision.transforms as transforms
from PIL import Image


class ObjectDetector():
    def __init__(self, project_name, model_directory="/model/setup") -> None:
        self.onnx_model = onnx.load(f"{model_directory}/{project_name}.onnx")
        onnx.checker.check_model(self.onnx_model)

        self.ort_session = rt.InferenceSession(f"{model_directory}/{project_name}.onnx", providers=["CPUExecutionProvider"])
        sess_options = rt.SessionOptions()
        sess_options.execution_mode = rt.ExecutionMode.ORT_PARALLEL

    def to_numpy(self, tensor):
        return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()

    
    def make_prediction(self, image):
        image = Image.open(image)
        image = image.convert('RGB')

        resize = transforms.Resize([1920, 1080])
        image = resize(image)
        
        to_tensor = transforms.ToTensor()
        image = to_tensor(image)
        image = image.unsqueeze(0)

        start = datetime.datetime.now()

        ort_inputs = {self.ort_session.get_inputs()[0].name: self.to_numpy(image)}
        ort_outs = self.ort_session.run(None, ort_inputs)
        logging.info(f"{datetime.datetime.now() - start}")

        return True, ort_outs[0].tolist()