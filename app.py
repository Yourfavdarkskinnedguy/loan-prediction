import os
from flask import Flask, render_template, request
import pickle
import numpy as np


app= Flask(__name__)

model_filepath= os.path.join(os.getcwd(), 'loan_model1.pkl')
scaler_filepath= os.path.join(os.getcwd(), 'loan_scaler.pkl')


model= pickle.load(open(model_filepath, 'rb'))
scaler= pickle.load(open(scaler_filepath, 'rb'))


@app.route("/", methods=["POST", "GET"])
def predict():
    if request.method == 'POST':
        try:
            #collecting the data from the form
            data = [float(x) for x in request.form.values()]
            print(f"Raw form data: {data}")

            #reshaping the collected data to the shape the model needs
            data_np= np.array(data).reshape(1,-1)
            print(data_np)
            
            #scaling the data 
            scaled_data = scaler.transform(data_np)
            print(f"Scaled data shape: {scaled_data.shape}")

            #making predictions
            prediction = model.predict(scaled_data)[0]
            result = "approved" if prediction==1 else "rejected"
            print(f"Prediction: {result}")


            return render_template('home.html', result=result)

        #for debugging
        except Exception as e:
            print(f"Error occurred: {e}")
            return render_template('home.html', result=None)

    return render_template('home.html')


if __name__ =='__main__':
    app.run(debug=True)