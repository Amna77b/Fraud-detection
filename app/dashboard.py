import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Détection de Fraude — Dashboard", layout="wide")

st.title("🔍 Dashboard de Détection d'Anomalies Financières")

df = pd.read_csv("data/creditcard_scored.csv")

col1, col2, col3 = st.columns(3)
col1.metric("Transactions totales", f"{len(df):,}")
col2.metric("Fraudes détectées (réelles)", int(df["Class"].sum()))
col3.metric("Taux de fraude", f"{df['Class'].mean()*100:.3f} %")

st.subheader("Répartition des montants par type de transaction")
fig = px.box(df[df["Amount"] < 500], x="Class", y="Amount",
             labels={"Class": "0 = Normal, 1 = Fraude"})
st.plotly_chart(fig, use_container_width=True)

st.subheader("Transactions dans le temps")
fig2 = px.histogram(df, x="Time", color="Class", nbins=50,
                     labels={"Class": "0 = Normal, 1 = Fraude"})
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Échantillon de transactions suspectes")
st.dataframe(df[df["Class"] == 1].head(20))