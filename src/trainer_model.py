import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, f1_score

def train_and_save_model(X_train, y_train, X_test, y_test, config):
    """
    Entrena y guarda el modelo según la configuración.
    Entrada: datos de entrenamiento/prueba + config (dict)
    Salida: dict con métricas {accuracy, recall, f1_score}
    """
    model_name = config['model']['name']

    # Fábrica de modelos
    if model_name == "RandomForest":
        model = RandomForestClassifier(
            n_estimators=config['model']['n_estimators'],
            max_depth=config['model']['max_depth'],
            random_state=42
        )
    elif model_name == "LogisticRegression":
        model = LogisticRegression(
            C=config['model']['C'],
            max_iter=1000,
            random_state=42
        )
    else:
        raise ValueError(f"Modelo no soportado: {model_name}")

    # Entrenar
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Métricas
    metrics = {
        "accuracy": round(accuracy_score(y_test, y_pred), 4),
        "recall": round(recall_score(y_test, y_pred), 4),
        "f1_score": round(f1_score(y_test, y_pred), 4)
    }

    # Guardar modelo
    os.makedirs(os.path.dirname(config['paths']['model_save']), exist_ok=True)
    joblib.dump(model, config['paths']['model_save'])
    print(f"Modelo guardado en: {config['paths']['model_save']}")
    print(f"Métricas: {metrics}")

    return metrics