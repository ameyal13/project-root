# src/api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import os

app = FastAPI(
    title="Churn Prediction API",
    description="API para predecir si un cliente de telecomunicaciones abandonará el servicio.",
    version="1.0.0"
)

MODEL_PATH = "models/model.pkl"

# Esquema de entrada: los mismos 30 features que usa el modelo
class CustomerFeatures(BaseModel):
    gender: int
    SeniorCitizen: int
    Partner: int
    Dependents_Yes: int
    tenure: float
    PhoneService_Yes: int
    MultipleLines_No_phone_service: int
    MultipleLines_Yes: int
    InternetService_Fiber_optic: int
    InternetService_No: int
    OnlineSecurity_No_internet_service: int
    OnlineSecurity_Yes: int
    OnlineBackup_No_internet_service: int
    OnlineBackup_Yes: int
    DeviceProtection_No_internet_service: int
    DeviceProtection_Yes: int
    TechSupport_No_internet_service: int
    TechSupport_Yes: int
    StreamingTV_No_internet_service: int
    StreamingTV_Yes: int
    StreamingMovies_No_internet_service: int
    StreamingMovies_Yes: int
    Contract_One_year: int
    Contract_Two_year: int
    PaperlessBilling_Yes: int
    PaymentMethod_Credit_card_automatic: int
    PaymentMethod_Electronic_check: int
    PaymentMethod_Mailed_check: int
    MonthlyCharges: float
    TotalCharges: float


def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"No se encontró el modelo en '{MODEL_PATH}'. "
            "Ejecuta primero: python -m src.main"
        )
    return joblib.load(MODEL_PATH)


@app.get("/")
def root():
    return {"message": "Churn Prediction API activa. Usa POST /predict para hacer predicciones."}


@app.post("/predict")
def predict(customer: CustomerFeatures):
    """
    Recibe los features de un cliente en JSON y devuelve:
    - prediction: 0 (no churn) o 1 (churn)
    - label: texto descriptivo
    - churn_probability: probabilidad de churn (0.0 - 1.0)
    """
    try:
        model = load_model()
    except FileNotFoundError as e:
        raise HTTPException(status_code=503, detail=str(e))

    # Mapeo: los nombres en Pydantic usan _ pero el modelo fue entrenado con espacios/paréntesis
    data = {
        'gender': customer.gender,
        'SeniorCitizen': customer.SeniorCitizen,
        'Partner': customer.Partner,
        'Dependents_Yes': customer.Dependents_Yes,
        'tenure': customer.tenure,
        'PhoneService_Yes': customer.PhoneService_Yes,
        'MultipleLines_No phone service': customer.MultipleLines_No_phone_service,
        'MultipleLines_Yes': customer.MultipleLines_Yes,
        'InternetService_Fiber optic': customer.InternetService_Fiber_optic,
        'InternetService_No': customer.InternetService_No,
        'OnlineSecurity_No internet service': customer.OnlineSecurity_No_internet_service,
        'OnlineSecurity_Yes': customer.OnlineSecurity_Yes,
        'OnlineBackup_No internet service': customer.OnlineBackup_No_internet_service,
        'OnlineBackup_Yes': customer.OnlineBackup_Yes,
        'DeviceProtection_No internet service': customer.DeviceProtection_No_internet_service,
        'DeviceProtection_Yes': customer.DeviceProtection_Yes,
        'TechSupport_No internet service': customer.TechSupport_No_internet_service,
        'TechSupport_Yes': customer.TechSupport_Yes,
        'StreamingTV_No internet service': customer.StreamingTV_No_internet_service,
        'StreamingTV_Yes': customer.StreamingTV_Yes,
        'StreamingMovies_No internet service': customer.StreamingMovies_No_internet_service,
        'StreamingMovies_Yes': customer.StreamingMovies_Yes,
        'Contract_One year': customer.Contract_One_year,
        'Contract_Two year': customer.Contract_Two_year,
        'PaperlessBilling_Yes': customer.PaperlessBilling_Yes,
        'PaymentMethod_Credit card (automatic)': customer.PaymentMethod_Credit_card_automatic,
        'PaymentMethod_Electronic check': customer.PaymentMethod_Electronic_check,
        'PaymentMethod_Mailed check': customer.PaymentMethod_Mailed_check,
        'MonthlyCharges': customer.MonthlyCharges,
        'TotalCharges': customer.TotalCharges,
    }

    df = pd.DataFrame([data])
    prediction = int(model.predict(df)[0])
    probability = float(model.predict_proba(df)[0][1])

    return {
        "prediction": prediction,
        "label": "CHURN (se va)" if prediction == 1 else "NO CHURN (se queda)",
        "churn_probability": round(probability, 4)
    }