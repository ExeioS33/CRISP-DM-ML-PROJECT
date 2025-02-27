# ML PROJECT using CRISP-DM methodology

## Case 1 : Predicting credit_risk (not deployed)

## Case 2 : Predicting heart disease class of patient

### Personal preferences and project structure choices

- I've used **uv** for pyhon env management and dependencies.
- Project structure with 3 main directories for the data science part (data, models and notebooks)
  and 1 directory (src) for the REST API service.

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

# Model prediction specificities and improvements

- I force the user to specify a random number of patients in the api http call which is not the good way to make a prediction.
- Behind I generate random synthetic patients data (it was for demonstration purposes) and the model makes prediction on this dataset.
- In the future, I will change the argument to pass in the http Post method to allow passing a full patient info. So the model predicts only for this specific patient if he's diseased or not.

# General project improvements

- Data preparation and modeling part are not accurate.
- The model only predicts heart diseased patient in the json response of the api calls on synthetic data 😂.
- utilities.ipynb contains my ML related functions library, it is actually deorganised and full of bad stuffs that need to be cleaned later on.

# Constraints

- The job had to be completed in less than 2 days which leads to precipitation in most of the steps of the CRISP-DM methodology.
- Lack of time for a deep understanding of business and data.

# Additional notes on commands.md

- This file contains different terminal commands to run the api service that exposes the model and the command to call it.
- The Dockerfile is based on an existing image that contains all the ML tools so we won't need to redownload all the dependencies again.
