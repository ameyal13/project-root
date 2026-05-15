import joblib
import pandas as pd
import os

def predict_single_customer(model_path="models/model.pkl"):
    """
    Carga el modelo y predice sobre un cliente de ejemplo.
    """
    # Manejo de error si no existe el modelo
    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"No se encontró el modelo en '{model_path}'. "
            "Ejecuta primero: python -m src.main"
        )

    model = joblib.load(model_path)

    # Cliente de ejemplo (valores numéricos ya codificados)
    customer = pd.DataFrame([{
        'gender': 1,
        'SeniorCitizen': 0,
        'Partner': 1,
        'Dependents_Yes': 0,
        'tenure': 12,
        'PhoneService_Yes': 1,
        'MultipleLines_No phone service': 0,
        'MultipleLines_Yes': 0,
        'InternetService_Fiber optic': 1,
        'InternetService_No': 0,
        'OnlineSecurity_No internet service': 0,
        'OnlineSecurity_Yes': 0,
        'OnlineBackup_No internet service': 0,
        'OnlineBackup_Yes': 1,
        'DeviceProtection_No internet service': 0,
        'DeviceProtection_Yes': 0,
        'TechSupport_No internet service': 0,
        'TechSupport_Yes': 0,
        'StreamingTV_No internet service': 0,
        'StreamingTV_Yes': 1,
        'StreamingMovies_No internet service': 0,
        'StreamingMovies_Yes': 1,
        'Contract_One year': 0,
        'Contract_Two year': 0,
        'PaperlessBilling_Yes': 1,
        'PaymentMethod_Credit card (automatic)': 0,
        'PaymentMethod_Electronic check': 1,
        'PaymentMethod_Mailed check': 0,
        'MonthlyCharges': 70.5,
        'TotalCharges': 846.0
    }])

    prediction = model.predict(customer)[0]
    probability = model.predict_proba(customer)[0][1]

    resultado = "CHURN (se va)" if prediction == 1 else "NO CHURN (se queda)"
    print(f"Predicción: {resultado}")
    print(f"Probabilidad de churn: {probability:.2%}")
    return prediction

if __name__ == "__main__":
    predict_single_customer()