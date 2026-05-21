# Proyecto MLOps: Predicción de Churn

Este proyecto entrena un modelo de Machine Learning para predecir si un cliente de telecomunicaciones abandonará el servicio. Usa el dataset Telco Customer Churn y ejecuta un pipeline básico de carga de datos, preprocesamiento, entrenamiento, evaluación y guardado del modelo.

## Dataset

El proyecto usa el dataset Telco Customer Churn de Kaggle.

Archivo requerido:

```text
WA_Fn-UseC_-Telco-Customer-Churn.csv
```

El archivo debe guardarse en:

```text
data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv
```

El dataset no se sube al repositorio porque la carpeta `data/` está ignorada en `.gitignore`.

## Instalación

Clona el repositorio:

```bash
git clone https://github.com/ameyal13/project-root.git
cd project-root
```

Crea un entorno virtual:

```bash
python -m venv venv
```

Activa el entorno virtual.

En Linux o macOS:

```bash
source venv/bin/activate
```

En Windows:

```bash
venv\Scripts\activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Configuración

Los parámetros principales se encuentran en:

```text
config/params.yaml
```

Desde ese archivo se controla:

- Ruta del dataset.
- Tamaño del conjunto de prueba.
- Semilla aleatoria.
- Modelo a entrenar.
- Hiperparámetros.
- Ruta donde se guarda el modelo.

## Cómo ejecutar el entrenamiento

Ejecuta el pipeline completo con:

```bash
python -m src.main
```

El script carga el dataset, limpia y transforma los datos, entrena el modelo configurado, calcula métricas y guarda el modelo en:

```text
models/model.pkl
```

Ejemplo de salida esperada:

```text
=== Pipeline de Churn MLOps ===

[1/2] Cargando y preprocesando datos...
Train: (5634, 30) | Test: (1409, 30)

[2/2] Entrenando modelo...
Modelo guardado en: models/model.pkl
Métricas: {'accuracy': 0.79, 'recall': 0.49, 'f1_score': 0.56}
```

Los valores pueden cambiar según el modelo y la configuración usada.

## Cómo ejecutar una predicción

Después de entrenar el modelo, ejecuta:

```bash
python -m src.predict
```

El script carga `models/model.pkl` y hace una predicción con un cliente de ejemplo definido en `src/predict.py`.

Ejemplo de salida:

```text
Predicción: CHURN (se va)
Probabilidad de churn: 62.35%
```

Si el modelo no existe, primero ejecuta:

```bash
python -m src.main
```

## Estructura principal

```text
project-root/
├── config/
│   └── params.yaml
├── data/
│   └── raw/
│       └── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── models/
│   └── model.pkl
├── src/
│   ├── data_loader.py
│   ├── main.py
│   ├── predict.py
│   └── trainer_model.py
├── ETHICS.md
├── requirements.txt
└── README.md
```

## API de Predicción

El proyecto incluye una API REST construida con FastAPI.

### Iniciar el servidor

```bash
uvicorn src.api:app --reload
```

El servidor queda disponible en `http://127.0.0.1:8000`.

La documentación interactiva (Swagger UI) estará en `http://127.0.0.1:8000/docs`.

> Asegúrate de haber entrenado el modelo primero con `python -m src.main`.

### Endpoint: `POST /predict`

Recibe los features de un cliente en JSON y devuelve la predicción.

**Ejemplo con `curl`:**

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "gender": 1,
       "SeniorCitizen": 0,
       "Partner": 1,
       "Dependents_Yes": 0,
       "tenure": 12,
       "PhoneService_Yes": 1,
       "MultipleLines_No_phone_service": 0,
       "MultipleLines_Yes": 0,
       "InternetService_Fiber_optic": 1,
       "InternetService_No": 0,
       "OnlineSecurity_No_internet_service": 0,
       "OnlineSecurity_Yes": 0,
       "OnlineBackup_No_internet_service": 0,
       "OnlineBackup_Yes": 1,
       "DeviceProtection_No_internet_service": 0,
       "DeviceProtection_Yes": 0,
       "TechSupport_No_internet_service": 0,
       "TechSupport_Yes": 0,
       "StreamingTV_No_internet_service": 0,
       "StreamingTV_Yes": 1,
       "StreamingMovies_No_internet_service": 0,
       "StreamingMovies_Yes": 1,
       "Contract_One_year": 0,
       "Contract_Two_year": 0,
       "PaperlessBilling_Yes": 1,
       "PaymentMethod_Credit_card_automatic": 0,
       "PaymentMethod_Electronic_check": 1,
       "PaymentMethod_Mailed_check": 0,
       "MonthlyCharges": 70.5,
       "TotalCharges": 846.0
     }'
```

**Ejemplo con `requests` (Python):**

```python
import requests

url = "http://127.0.0.1:8000/predict"

customer = {
    "gender": 1,
    "SeniorCitizen": 0,
    "Partner": 1,
    "Dependents_Yes": 0,
    "tenure": 12,
    "PhoneService_Yes": 1,
    "MultipleLines_No_phone_service": 0,
    "MultipleLines_Yes": 0,
    "InternetService_Fiber_optic": 1,
    "InternetService_No": 0,
    "OnlineSecurity_No_internet_service": 0,
    "OnlineSecurity_Yes": 0,
    "OnlineBackup_No_internet_service": 0,
    "OnlineBackup_Yes": 1,
    "DeviceProtection_No_internet_service": 0,
    "DeviceProtection_Yes": 0,
    "TechSupport_No_internet_service": 0,
    "TechSupport_Yes": 0,
    "StreamingTV_No_internet_service": 0,
    "StreamingTV_Yes": 1,
    "StreamingMovies_No_internet_service": 0,
    "StreamingMovies_Yes": 1,
    "Contract_One_year": 0,
    "Contract_Two_year": 0,
    "PaperlessBilling_Yes": 1,
    "PaymentMethod_Credit_card_automatic": 0,
    "PaymentMethod_Electronic_check": 1,
    "PaymentMethod_Mailed_check": 0,
    "MonthlyCharges": 70.5,
    "TotalCharges": 846.0
}

response = requests.post(url, json=customer)
print(response.json())
```

**Respuesta esperada:**

```json
{
  "prediction": 1,
  "label": "CHURN (se va)",
  "churn_probability": 0.6235
}
```
