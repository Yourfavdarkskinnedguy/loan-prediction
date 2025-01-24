# Loan Prediction System

## Overview
This is a **Loan Prediction System** designed to predict whether a loan application will be approved or not based on certain applicant features. The project uses a dataset from Kaggle, implements data cleaning and preprocessing, and utilizes a Flask API for backend integration with an HTML-based frontend.

## Features
- Predicts loan approval status based on user inputs.
- Cleaned and preprocessed dataset for improved model performance.
- Flask API for backend predictions.
- User-friendly HTML interface for data input and displaying results.

## Dataset
The dataset was obtained from Kaggle and contains features such as:
- person age
- person gender
- Loan Amount
- Credit History
- person income
- Loan intent
- Education level
- Gender, and more.

**Data Cleaning Tasks:**
- Handled missing values.
- Encoded categorical variables.
- Scaled numerical features for consistency.

[Link to Dataset](#) (https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data)

## Data Cleaning and Preprocessing

1. **Feature Engineering:**
   - Removed redundant or irrelevant columns.

2. **Scaling and Encoding:**
   - Normalized numerical data for consistency.
   - Applied label encoding for categorical variables.

## Tech Stack
- **Programming Languages:** Python, HTML
- **Backend Framework:** Flask
- **Frontend:** HTML, CSS
- **Libraries and Tools:**
  - Pandas, NumPy (for data cleaning and manipulation)
  - Scikit-learn (for model training and evaluation)
  - Flask (for backend API)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/loan-prediction.git

## Navigate to the directory
cd loan-prediction

## Installed the required dependencies
pip install -r requirements.txt

## Run the flask application 
python app.py

## link to the webapp

[Loan Predictor] (https://loan-prediction-4z1y.onrender.com/)


