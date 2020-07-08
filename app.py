import numpy as np
from flask import Flask, request, jsonify, render_template
from joblib import load
app = Flask(__name__)
model = load('RFR.save')

@app.route('/')
def home():
    return render_template('proj.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[float(x) for x in request.form.values()]]
    if(x_test[0][0] == 0):
        x_test[0][0]=0
        x_test[0].insert(1,0)
        x_test[0].insert(2,1)
    elif(x_test[0][0] == 1):
        x_test[0][0]=0
        x_test[0].insert(1,1)
        x_test[0].insert(2,0)
    elif(x_test[0][0] == 2):
        x_test[0][0]=1
        x_test[0].insert(1,0)
        x_test[0].insert(2,0)
    else:
        x_test[0][0]=0
        x_test[0].insert(1,0)
        x_test[0].insert(2,0)
    print(x_test)
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0]
    
    return render_template('proj1.html', prediction_text = output)
          
if __name__ == "__main__":
    app.run(debug=True)
