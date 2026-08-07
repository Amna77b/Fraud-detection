import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import joblib

def train_model():
    df = pd.read_csv("data/creditcard.csv")

    # Normalisation du montant et du temps (les autres colonnes sont déjà normalisées via PCA)
    scaler = StandardScaler()
    df["Amount_scaled"] = scaler.fit_transform(df[["Amount"]])
    df["Time_scaled"] = scaler.fit_transform(df[["Time"]])

    features = [c for c in df.columns if c.startswith("V")] + ["Amount_scaled", "Time_scaled"]
    X = df[features]
    y = df["Class"]

    # contamination = proportion attendue d'anomalies (~0.17% ici)
    model = IsolationForest(n_estimators=200, contamination=0.0017, random_state=42)
    model.fit(X)

    # IsolationForest renvoie -1 (anomalie) / 1 (normal) -> on convertit en 1/0 pour comparer à y
    predictions = model.predict(X)
    predictions = [1 if p == -1 else 0 for p in predictions]

    print(classification_report(y, predictions))

    joblib.dump(model, "app/isolation_forest.pkl")
    joblib.dump(scaler, "app/scaler.pkl")
    df.to_csv("data/creditcard_scored.csv", index=False)
    print("Modèle sauvegardé.")

if __name__ == "__main__":
    train_model()