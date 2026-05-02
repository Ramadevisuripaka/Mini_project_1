from flask import Flask, request, render_template
from main import MLR   # your file name (main.py)
import numpy as np

app = Flask(__name__)

# Load model once
obj = MLR('House.csv')
obj.training()

@app.route('/')
def home():
    return render_template('index.html')   # create this HTML file

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from form
        bedrooms = float(request.form['bedrooms'])
        bathrooms = float(request.form['bathrooms'])
        sqft_living = float(request.form['sqft_living'])
        sqft_lot = float(request.form['sqft_lot'])
        floors = float(request.form['floors'])
        waterfront = int(request.form['waterfront'])
        view = int(request.form['view'])
        condition = int(request.form['condition'])
        sqft_above = float(request.form['sqft_above'])
        sqft_basement = float(request.form['sqft_basement'])
        yr_built = int(request.form['yr_built'])
        yr_renovated = int(request.form['yr_renovated'])
        city = int(request.form['city'])
        country = int(request.form['country'])

        # Prepare input
        features = [[bedrooms, bathrooms, sqft_living, sqft_lot, floors,
                     waterfront, view, condition, sqft_above, sqft_basement,
                     yr_built, yr_renovated, city, country]]

        # Prediction
        prediction = obj.reg.predict(features)

        return render_template('index.html', prediction_text=f'Price Prediction: {prediction[0]}')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)