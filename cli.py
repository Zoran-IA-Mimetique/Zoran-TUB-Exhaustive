import argparse, os
from transform_csv_to_dataframe import transform_csv_to_dataframe
from calc_scores import main as calc_main
from update_risk_register_template import update_risk_register_template

def ensure_out():
    os.makedirs('out', exist_ok=True)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='TUB CLI — Zoran')
    sub = ap.add_subparsers(dest='cmd')

    v = sub.add_parser('validate', help='Valide un CSV selon le schéma')
    v.add_argument('--csv', required=True)

    s = sub.add_parser('scores', help='Calcule V(x) et ajoute la colonne V_conf')
    s.add_argument('--csv', required=True)
    s.add_argument('--out', default='out/risk_scores.csv')

    u = sub.add_parser('update-template', help='Remplit le modèle Excel')
    u.add_argument('--excel', required=True)
    u.add_argument('--csv', required=True)
    u.add_argument('--sheet', default='Risks')
    u.add_argument('--header-row', type=int, default=1)
    u.add_argument('--start-col', type=int, default=1)
    u.add_argument('--out', default='out/updated_risk_register.xlsx')
    u.add_argument('--include-headers', action='store_true')

    args = ap.parse_args()
    ensure_out()

    if args.cmd == 'validate':
        df = transform_csv_to_dataframe(args.csv)
        print('✅ CSV valide:', df.shape, 'lignes/colonnes')
    elif args.cmd == 'scores':
        calc_main(args.csv, args.out)
    elif args.cmd == 'update-template':
        update_risk_register_template(args.excel, args.csv, args.sheet, args.header_row, args.start_col, args.out, args.include_headers)
    else:
        ap.print_help()