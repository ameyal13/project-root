import pytest
import yaml
from src.data_loader import load_and_preprocess_data
from src.trainer_model import train_and_save_model

@pytest.fixture
def config():
    with open("config/params.yaml", "r") as f:
        return yaml.safe_load(f)

def test_load_data_not_empty(config):
    """Verifica que los datos cargados no estén vacíos."""
    X_train, X_test, y_train, y_test = load_and_preprocess_data(config)
    
    assert len(X_train) > 0, "X_train está vacío"
    assert len(X_test) > 0, "X_test está vacío"
    assert len(y_train) > 0, "y_train está vacío"
    assert len(y_test) > 0, "y_test está vacío"

def test_model_returns_metrics(config):
    """Verifica que el modelo devuelva las 3 métricas requeridas."""
    X_train, X_test, y_train, y_test = load_and_preprocess_data(config)
    metrics = train_and_save_model(X_train, y_train, X_test, y_test, config)
    
    assert "accuracy" in metrics, "Falta métrica: accuracy"
    assert "recall" in metrics, "Falta métrica: recall"
    assert "f1_score" in metrics, "Falta métrica: f1_score"
    assert 0 <= metrics["accuracy"] <= 1
    assert 0 <= metrics["recall"] <= 1
    assert 0 <= metrics["f1_score"] <= 1