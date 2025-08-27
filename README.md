# Zoran — TUB (Total Utility Base) · Dépôt Exhaustif & Validé

> Objectif : fournir un **registre des risques opérationnel**, **validé par l'équipe**, avec **données d'exemple**, **scripts robustes**, **tests**, **CI/CD**, **modèles Excel**, **documentation** et **procédures** pour être **crédible et prêt à l'audit**.

## ⚡ Contenu clé
- `data/` : CSV d'exemple **valides** et **invalides** pour tester les scripts.
- `scripts/` : transformation CSV→DataFrame, mise à jour de template Excel, calcul V(x), CLI unifiée.
- `templates/` : modèle Excel (`risk_register_template.xlsx`) prêt à remplir.
- `tests/` : tests **pytest** couvrant parsing, validation schéma, calcul V(x).
- `config/config.yaml` : schéma attendu des colonnes + mapping vers V(x).
- `meta/descriptors/` : résumés **150 / 350 / 8000**.
- `.github/workflows/ci.yml` : lint + tests + audit dépendances.
- `docs/` : guide d'utilisation, RACI de validation, checklists d'acceptation.
- `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `CHANGELOG.md`.

## 🚀 Quickstart
```bash
# 1) Installer (Python 3.11+)
pip install -r requirements.txt

# 2) Lancer les tests
pytest -q

# 3) Calculer les scores V(x) sur data/risk_data_example.csv
python scripts/calc_scores.py --csv data/risk_data_example.csv --out out/risk_scores.csv

# 4) Mettre à jour le modèle Excel
python scripts/update_risk_register_template.py   --excel templates/risk_register_template.xlsx   --csv data/risk_data_example.csv   --sheet 'Risks' --header-row 1 --start-col 1   --out out/updated_risk_register.xlsx
```

## 🧠 V(x) — Fonction de risque
- **Définition** : transforme un vecteur de facteurs de risque en **score 0–100** (voir `scripts/vx.py` + `docs/Vx.md`).
- **Seuils** : V<20 (surveillance), 20–40 (corriger en sprint), 40–60 (prioritaire), ≥60 (**bloquant CI/CD**).

## ✅ Validation & Acceptation (RACI)
- **R** (Responsible) : data owner vérifie la qualité CSV.
- **A** (Accountable) : chef de projet approuve la version publiée.
- **C** (Consulted) : sécurité & conformité relisent.
- **I** (Informed) : toutes les parties prenantes reçoivent le rapport de CI.
Voir `docs/acceptance_checklist.md` et `docs/raci.md`.

## 🔐 Sécurité & Conformité
- RGPD : pseudonymisation & TTL (cf. `scripts/rgpd_tools.py`), journal Merkle dans le dépôt Zoran Risk Register.
- AI Act / ISO 27005/27001 : champs et processus alignés.
- CI : `pip-audit`, tests & seuil V(x) configurable.

## 🧾 Licence & Contact
MIT — public good. Contact : tabary01@gmail.com