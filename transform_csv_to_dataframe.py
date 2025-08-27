import pandas as pd
import yaml
import sys

def load_config(path='config/config.yaml'):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def validate_dataframe(df: pd.DataFrame, cfg: dict) -> None:
    req = cfg['schema']['required_columns']
    missing = [c for c in req if c not in df.columns]
    if missing:
        raise ValueError(f"Colonnes manquantes: {missing}")
    # Optionally enforce dtypes
    dtypes = cfg['schema'].get('dtypes', {})
    for col, typ in dtypes.items():
        if col in df.columns and typ in ('float','int'):
            df[col] = pd.to_numeric(df[col], errors='coerce')
    if df[req].isnull().any().any():
        raise ValueError("Valeurs nulles détectées dans des colonnes requises.")

def transform_csv_to_dataframe(csv_file_path: str, config_path='config/config.yaml') -> pd.DataFrame:
    df = pd.read_csv(csv_file_path)
    cfg = load_config(config_path)
    validate_dataframe(df, cfg)
    return df

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'data/risk_data_example.csv'
    df = transform_csv_to_dataframe(path)
    print(df.head().to_string(index=False))