from flask import Flask, render_template, request
import numpy as np
import mlflow
import sklearn
from mlflow.tracking import MlflowClient

#create an instance of Flask
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict/', methods=['GET','POST'])
def predict():
    
    if request.method == "POST":
        #get form data
        sepal_length = request.form.get('sepal_length')
        sepal_width = request.form.get('sepal_width')
        petal_length = request.form.get('petal_length')
        petal_width = request.form.get('petal_width')
        
        #call preprocessDataAndPredict and pass inputs
        try:
            prediction = preprocessDataAndPredict(sepal_length,       sepal_width, petal_length, petal_width)
            #pass prediction to template
            return render_template('predict.html', prediction = prediction)
   
        except ValueError:
            return "Please Enter valid values"
  
        pass
    pass
def preprocessDataAndPredict(sepal_length, sepal_width, petal_length, petal_width):
    
    #keep all inputs in array
    test_data = [sepal_length, sepal_width, petal_length, petal_width]

    #convert value data into numpy array
    test_data = np.array(test_data)
    
    #reshape array
    test_data = test_data.reshape(1,-1)
    
    #load trained model from Mlflow

    remote_server_uri = "http://52.67.153.88:5000/" # set to your server URI
    mlflow.set_tracking_uri(remote_server_uri)
    client = MlflowClient()
    prod_model = client.get_latest_versions(name = "RFClassifierModel",
                           stages = ["Production"])

    trained_model = mlflow.sklearn.load_model(dict(prod_model[0])["source"])

    prediction = trained_model.predict(test_data)

    return prediction
    
    pass

@app.route('/model/', methods=['GET'])
def modelInfo():
    remote_server_uri = "http://52.67.153.88:5000/" # set to your server URI
    mlflow.set_tracking_uri(remote_server_uri)
    mlflow.set_experiment("cd4ml")
    
    client = MlflowClient()
    prod_model = client.get_latest_versions(name = "RFClassifierModel",
                        stages = ["Production"])

    mlflow.end_run()

    return dict(prod_model[0])
if __name__ == '__main__':
    app.run(debug=True)
   