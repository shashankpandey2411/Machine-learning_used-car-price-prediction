
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import joblib as joblib
from joblib import load
app = Flask(__name__)
# model = pickle.load(open('d.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    
    x_test = [[int(x) for x in request.form.values()]]
    print(x_test)
    scaler=load('scalar8.save')
    xgb  = joblib.load('model.pkl')
    prediction = xgb.predict(x_test)
    print(prediction)
    output=prediction[0]
    ans= round(output,2)
    # output = 500000
    return render_template('index.html', prediction_text=ans)

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])

    output = prediction[0]
    
  
    return jsonify(round(output,2))

if __name__ == "__main__":
    app.run(debug=True)