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

## Notas

Este proyecto no incluye una API. La ejecución disponible es por línea de comandos mediante `src.main` y `src.predict`.
