# Financial Anomaly Detection & BI Dashboard

Credit card fraud detection project combining unsupervised and supervised
Machine Learning with interactive visualization — applying a Data & AI
consulting lens (audit augmented by data analytics).

## Stack
- Python, Scikit-learn (Isolation Forest)
- XGBoost, imbalanced-learn (SMOTE) — supervised model with risk scoring
- Streamlit + Plotly (interactive dashboard)
- Pandas, Seaborn (exploratory analysis)

## Dataset
[Credit Card Fraud Detection (Kaggle, ULB)](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
— download separately and place in `data/creditcard.csv`
(not included in this repo per Kaggle's usage terms).

## Run the project
```bash
pip install -r requirements.txt
python app/model.py                # unsupervised model (Isolation Forest)
python app/model_supervised.py     # supervised model (XGBoost + SMOTE)
streamlit run app/dashboard.py
```

## Deliverables
- `notebooks/01_exploration.ipynb` — exploratory data analysis
- `app/dashboard.py` — interactive dashboard with adjustable risk threshold
- `reports/consulting_note_en.md` — business summary and recommendations

*[Version française](README.md)*