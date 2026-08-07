# Détection d'Anomalies Financières & Dashboard BI

Projet de détection de fraude sur transactions bancaires, combinant Machine
Learning non supervisé et visualisation interactive — dans une logique
Data & IA appliquée au conseil (audit augmenté par la donnée).

## Stack
- Python, Scikit-learn (Isolation Forest)
- Streamlit + Plotly (dashboard)
- Pandas, Seaborn (exploration)

## Dataset
[Credit Card Fraud Detection (Kaggle, ULB)](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
— à télécharger séparément et placer dans `data/creditcard.csv`
(non inclus dans ce repo pour respecter les conditions d'usage Kaggle).

## Lancer le projet
\`\`\`bash
pip install -r requirements.txt
python app/model.py
streamlit run app/dashboard.py
\`\`\`

## Livrables
- `notebooks/01_exploration.ipynb` — analyse exploratoire
- `app/dashboard.py` — dashboard interactif
- `reports/note_conseil.md` — synthèse et recommandations business