import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_preprocess_data(config):
    #Carga y preprocesa el dataset de Telco Customer Churn.
   
    # Cargar CSV
    df = pd.read_csv(config['data']['raw_path'])

    # Limpiar TotalCharges: convertir a numérico, espacios vacíos -> NaN -> mediana
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())  
    
    df = df.drop(columns=['customerID'])
    # Codificar columnas binarias
    df['gender'] = df['gender'].map({'Male': 1, 'Female': 0})
    df['Partner'] = df['Partner'].map({'Yes': 1, 'No': 0})
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    # Codificar el resto de columnas categóricas con get_dummies
    df = pd.get_dummies(df, drop_first=True)

    # Separar features y target
    X = df.drop(columns=['Churn'])
    y = df['Churn']

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=config['data']['test_size'],
        random_state=config['data']['random_state']
    )

    return X_train, X_test, y_train, y_test