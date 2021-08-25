from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from utils.utils import decodeImage
from predict import traffic

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


#@cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = traffic(self.filename)



@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')
    


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.trafficsign()
    return jsonify(result)


#
if __name__ == "__main__":
    clApp = ClientApp()
    port = int(os.getenv("PORT"))
    host = '0.0.0.0'
    #port = 6000
    httpd = simple_server.make_server(host=host, port = port, app = app)
    #print("Serving on %s %d" % (host, port))
    httpd.serve_forever()