import flask
from flask import Flask, jsonify, request
import json
import pickle
import numpy as np

app = Flask(__name__)

def load_models():
    file_name = "models/full_model.p"
    with open(file_name, 'rb') as pickled:
       data = pickle.load(pickled)
       model = data['model']
    return model

@app.route('/predict', methods=['GET'])

def predict():
    # stub input features
    # parse input features from request
    request_json = request.get_json()
    x = request_json['input']
    x_in = np.array (x).reshape (1, -1)
    # load model
    model = load_models()
    prediction = str(model.predict(x_in)[0])
    print (prediction)
    
    response = json.dumps({'response': prediction})
    return response, 200

if __name__ == '__main__':
    app.run(debug=True)
 
