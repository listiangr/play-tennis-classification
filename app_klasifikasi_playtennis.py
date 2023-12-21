from flask import Flask, request, render_template
import pickle
import pandas as pd 
import numpy as np 

app = Flask(__name__)

model_file = open('model_playTennis.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', hasil=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    outlook = int(request.form['outlook'])
    temp = int(request.form['temp'])
    humidity = int(request.form['humidity'])
    wind = int(request.form['wind'])
    
    x = np.array([[outlook, temp, humidity, wind]])
    
    prediction = model.predict(x)
    outlooks = ['Overcast', 'Rain', 'Sunny']
    temps = ['Cool', 'Hot', 'Mild']
    humiditys = ['High', 'Normal']
    winds = ['Strong', 'Weak']
    if(prediction == 0):
        play = "Tidak Bisa Bermain!"
    elif(prediction == 1):
        play = "Bisa Bermain!"
    

    return render_template('index.html', hasil=play, outlook=outlooks[outlook], temp=temps[temp], humidity=humiditys[humidity], wind=winds[wind])
    
if __name__ == '__main__':
    app.run(debug=True)
    