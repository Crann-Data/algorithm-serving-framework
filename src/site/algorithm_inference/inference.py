import datetime
import logging

import numpy as np
import onnx
import onnxruntime as rt
from PIL import Image


class ObjectDetector():
    def __init__(self, project_name, model_directory="/model/setup") -> None:
        self.onnx_model = onnx.load(f"{model_directory}/{project_name}.onnx")
        onnx.checker.check_model(self.onnx_model)

        sess_opt = rt.SessionOptions()
        sess_opt.intra_op_num_threads = 4

        self.ort_session = rt.InferenceSession(f"{model_directory}/{project_name}.onnx", sess_opt, providers=rt.get_available_providers())

    def to_numpy(self, tensor):
        return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()
    
    def make_prediction(self, image):
        image = Image.open(image)
        image = image.convert('RGB')

        image = image.resize((1920, 1080))
        image = np.array(image).astype(np.float32)
        image = image / 255
        image= np.transpose(image, (2, 0, 1))
        image = np.expand_dims(image, axis=0)

        start = datetime.datetime.now()

        ort_inputs = {self.ort_session.get_inputs()[0].name: image}
        ort_outs = self.ort_session.run(None, ort_inputs)
        logging.info(f"{datetime.datetime.now() - start}")        

        return True, ort_outs[0].tolist()