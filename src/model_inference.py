# src/model_inference.py

import joblib
import logging
import pandas as pd

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class HeartDiseaseModel:
    def __init__(self, model_path: str):
        # Load the trained model
        self.model = joblib.load(model_path)
        logger.info(f"Model loaded from {model_path}")

    def predict(self, df: pd.DataFrame):
        prediction = self.model.predict(df)  # e.g. array([0,1,0,1,...])
        probabilities = self.model.predict_proba(df)  # e.g. [[p0,p1],[p0,p1],...]

        results = []
        for pred, proba in zip(prediction, probabilities):
            # Convert numeric prediction to human-readable string
            label = "heart_disease" if pred == 1 else "normal"

            results.append(
                {
                    "prediction": label,
                    "heart_disease_probability": round(float(proba[1]), 4),
                }
            )
        return results
