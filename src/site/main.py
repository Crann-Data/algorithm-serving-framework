import logging

from algorithm_inference.inference import ObjectDetector

logging.basicConfig(format='%(levelname)s:%(asctime)s:%(funcName)s:%(message)s', level=logging.INFO)

od = ObjectDetector("prebuilt", "./algorithm/")

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
        
        return {'objects': str(data)}, 200

if __name__ == "__main__":
    create_app().run(debug=True, host="0.0.0.0", port=4000)

