from flask import Flask ,request,jsonify ,render_template 
import os 
from flask_cors import CORS ,cross_origin
from cnnClassifier.utils import decodeImage
from cnnClassifier.pipeline.predict import DogCat


os.putenv('LANG','en_US.UTF-8')
os.putenv('LC_ALL','en_US.UTF-8')

app=Flask(__name__)

CORS(app)

class ClientApp:
    def __init__(self):
        self.filename="inputImage.jpg"
        self.classifier=DogCat(self.filename)



@app.route("/",methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/train",methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done successfully !"

@app.route('/predict',methods=['POST'])
@cross_origin()
def predictRoute():
    image=request.json['image']
    decodeImage(image,clApp.filename)
    result=clApp.classifier.predictiondogcat()
    print("result is :",result[0])
    result=result[0]
    return jsonify(result)


if __name__=='__main__':
    clApp=ClientApp()
    app.run(host="0.0.0.0",port=8080)