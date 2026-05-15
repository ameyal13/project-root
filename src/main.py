import yaml
from src.data_loader import load_and_preprocess_data
from src.trainer_model import train_and_save_model

def main():
    # Cargar configuración
    with open("config/params.yaml", "r") as f:
        config = yaml.safe_load(f)

    print("=== Pipeline de Churn MLOps ===")
    
    # Paso 1: Cargar y preprocesar datos
    print("\n[1/2] Cargando y preprocesando datos...")
    X_train, X_test, y_train, y_test = load_and_preprocess_data(config)
    print(f"Train: {X_train.shape} | Test: {X_test.shape}")

    # Paso 2: Entrenar y guardar modelo
    print("\n[2/2] Entrenando modelo...")
    metrics = train_and_save_model(X_train, y_train, X_test, y_test, config)

    print("\n=== Resultados finales ===")
    for k, v in metrics.items():
        print(f"  {k}: {v}")

if __name__ == "__main__":
    main()