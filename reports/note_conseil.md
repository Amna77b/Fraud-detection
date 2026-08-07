# Note de synthèse — Détection d'anomalies financières

## Contexte
Analyse de 284 807 transactions par carte bancaire afin d'identifier les
transactions frauduleuses grâce à des techniques de Machine Learning non supervisé.

## Méthodologie
- Modèle : Isolation Forest (détection d'anomalies sans nécessiter d'exemples
  étiquetés de fraude au préalable — pertinent pour des cas réels où les
  nouvelles typologies de fraude sont inconnues à l'avance).
- Variables utilisées : montant, temporalité, et composantes issues d'une
  réduction de dimension (PCA) pour préserver la confidentialité des données
  bancaires.

## Résultats clés
- [Complète avec tes propres chiffres après exécution : rappel, précision]
- Les fraudes présentent [tendance observée sur les montants/temporalité].

## Recommandations business
1. Mettre en place un système d'alerte en temps réel sur les transactions
   scorées à risque, avec un seuil ajustable selon l'appétit au risque du client.
2. Prioriser la revue manuelle des transactions à fort montant + score
   d'anomalie élevé (optimisation des ressources d'audit).
3. Réentraîner le modèle périodiquement pour s'adapter à l'évolution des
   typologies de fraude.

## Limites
- Modèle non supervisé : pas de garantie de détecter 100% des fraudes connues.
- Dataset historique (2013) : les patterns de fraude évoluent, un déploiement
  réel nécessiterait un réentraînement sur données récentes.