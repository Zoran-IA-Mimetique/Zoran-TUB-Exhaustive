from scripts.calc_scores import main as calc_main
import pandas as pd, os

def test_scores(tmp_path):
    out = tmp_path/'scores.csv'
    calc_main('data/risk_data_example.csv', str(out))
    df = pd.read_csv(out)
    assert 'V_conf' in df.columns
    assert df['V_conf'].between(0,100).all()