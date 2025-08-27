import pandas as pd
from scripts.transform_csv_to_dataframe import transform_csv_to_dataframe

def test_valid_csv():
    df = transform_csv_to_dataframe('data/risk_data_example.csv')
    assert 'Risk' in df.columns
    assert len(df) >= 1

def test_invalid_csv_raises(tmp_path):
    import pytest
    from scripts.transform_csv_to_dataframe import load_config
    # change config to require a non-existing column to force failure
    cfg = load_config()
    required = cfg['schema']['required_columns']
    cfg['schema']['required_columns'] = required + ['NON_EXISTENT_COL']
    p = tmp_path/'cfg.yaml'
    import yaml
    p.write_text(yaml.safe_dump(cfg), encoding='utf-8')
    with pytest.raises(Exception):
        transform_csv_to_dataframe('data/risk_data_invalid.csv', config_path=str(p))