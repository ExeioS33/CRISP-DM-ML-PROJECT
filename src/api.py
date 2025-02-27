# src/api.py

import logging
import numpy as np
import pandas as pd
from fastapi import APIRouter
from src.model_inference import HeartDiseaseModel
from src.schemas import SyntheticRequest

router = APIRouter()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Initialize the model once
model_inference = HeartDiseaseModel("models/RandomForest_20250129_154514.pkl")


@router.post("/predict")
def predict_synthetic(data: SyntheticRequest):
    """
    Generates 'data.num_patients' synthetic patient records,
    feeds them into the model, and returns predictions.
    """
    num_patients = data.num_patients
    logger.info(f"Generating synthetic data for {num_patients} patients.")

    # Generate random data
    synthetic_data = pd.DataFrame(
        {
            "sex": np.random.choice([0, 1], size=num_patients),
            "weight": np.random.uniform(50, 100, size=num_patients),
            "height": np.random.uniform(150, 200, size=num_patients),
            "resting_bp_s": np.random.randint(90, 180, size=num_patients),
            "cholesterol": np.random.randint(150, 300, size=num_patients),
            "fasting_blood_sugar": np.random.choice([0, 1], size=num_patients),
            "physical_activity": np.random.randint(0, 4, size=num_patients),
            "age": np.random.randint(30, 80, size=num_patients),
            "ST_slope": np.random.randint(0, 3, size=num_patients),
            "chest_pain_type": np.random.randint(0, 4, size=num_patients),
            "exercise_angina": np.random.choice([0, 1], size=num_patients),
            "max_heart_rate": np.random.randint(100, 200, size=num_patients),
            "oldpeak": np.random.uniform(0, 5, size=num_patients),
            "resting_ecg": np.random.randint(0, 2, size=num_patients),
        }
    )

    # Call model
    predictions = model_inference.predict(synthetic_data)
    logger.info(f"Generated {num_patients} predictions.")

    return {"num_patients": num_patients, "predictions": predictions}
