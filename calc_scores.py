import argparse, pandas as pd, yaml, os
from vx import compute_vx

def load_config(path='config/config.yaml'):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def main(csv_path, out_path, config_path='config/config.yaml'):
    cfg = load_config(config_path)
    df = pd.read_csv(csv_path)
    # map cols
    params_cols = cfg['vx_mapping']
    scores = []
    for _, row in df.iterrows():
        params = {k: row[v] for k, v in params_cols.items() if v in row}
        res = compute_vx(params)
        scores.append(res['V_conf'])
    df['V_conf'] = scores
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"✅ Scores calculés → {out_path}")

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--csv', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--config', default='config/config.yaml')
    args = ap.parse_args()
    main(args.csv, args.out, args.config)