import logging

import torch
import torchvision
from flask import Flask, Response, jsonify, request
from flask_restful import Api, Resource
from PIL import Image

from algorithm_inference.inference import ObjectDetector

# from algorithm_factory.factory import ObjectDetector


logging.basicConfig(format='%(levelname)s:%(asctime)s:%(funcName)s:%(message)s', level=logging.INFO)


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Predict, '/')
    return app


class Predict(Resource):

    def post(self):
        if 'file' not in request.files:
            return Response('No file', 400)
        file = request.files['file']

        success, data = od.make_prediction(file)
        if not success:
            return Response(data, 500)
        
        return {'objects': str(data)}

if __name__ == "__main__":
    # image = Image.open("test/test-image.jpg")
    # image = image.convert('RGB')
    # convert_to_tensor = torchvision.transforms.ToTensor()
    # image = convert_to_tensor(image)
    # resize = torchvision.transforms.Resize([1920, 1080])
    # image = resize(image)

    # image = image.unsqueeze(0)
    # image = image.to(device="cuda")

    # od = ObjectDetector("testing", image, "./test/")


    od = ObjectDetector("testing", "./test/")
    create_app().run(debug=True, host="0.0.0.0", port=4000)

