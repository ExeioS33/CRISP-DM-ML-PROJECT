# ML Project Using CRISP-DM Methodology

## Case 1: Predicting Credit Risk (Not Deployed)

## Case 2: Predicting Heart Disease Class of Patients

### Personal Preferences and Project Structure Choices

- I've used **uv** for Python environment management and dependencies.
- The project structure includes 3 main directories for the data science part (data, models, and notebooks) and 1 directory (src) for the REST API service.

```bash
.
├── Dockerfile
├── README.md
├── commands.md
├── data
│   ├── DSA-2024_HeartDisease_Diagnosis_20240312.csv
│   ├── DSA-2024_HeartDisease_GeneralExams_20240312.tsv
│   ├── DSA-2024_HeartDisease_HeartExams_20240312.tsv
│   ├── credit_risk.csv
│   ├── encoded_dataset.csv
│   ├── merged_dataset.csv
│   ├── prepared_dataset.csv
│   └── test_properties.tsv
├── models
│   └── RandomForest_20250129_154514.pkl # saved model
├── notebooks
│   ├── credit_risk_analysis.ipynb
│   ├── feature_selection.ipynb
│   ├── generate_synthetic_data.ipynb
│   ├── heart_rate_diseased.ipynb
│   ├── model_training.ipynb
│   ├── model_training_bis.ipynb
│   └── utilities.ipynb
├── pyproject.toml
├── requirements.txt
├── response.json
├── src
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── api.cpython-312.pyc
│   │   ├── main.cpython-312.pyc
│   │   ├── model_inference.cpython-312.pyc
│   │   └── schemas.cpython-312.pyc
│   ├── api.py
│   ├── main.py
│   ├── model_inference.py
│   └── schemas.py
├── utilities.py
└── uv.lock
```

# Model Prediction Specificities and Improvements

- Currently, the user is required to specify a random number of patients in the API HTTP call, which is not the best way to make a prediction.
- For demonstration purposes, I generate random synthetic patient data, and the model makes predictions on this dataset.
- In the future, I plan to change the argument passed in the HTTP POST method to allow passing full patient information so the model can predict if this specific patient has a disease or not.

# General Project Improvements

- The data preparation and modeling parts are not accurate.
- The model only predicts heart disease in the JSON response of the API calls on synthetic data 😂.
- `utilities.ipynb` contains my ML-related functions library, which is currently disorganized and full of bad practices that need to be cleaned up later.

# Constraints

- The job had to be completed in less than 2 days, leading to rushed steps in the CRISP-DM methodology.
- There was a lack of time for a deep understanding of the business and data.

# Additional Notes on `commands.md`

- This file contains different terminal commands to run the API service that exposes the model and the command to call it.
- The Dockerfile is based on an existing image that contains all the ML tools, so we don't need to redownload all the dependencies again.
