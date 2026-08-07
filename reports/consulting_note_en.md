# Summary Note — Financial Anomaly Detection

## Context
Analysis of 284,807 credit card transactions to identify fraudulent
transactions using unsupervised and supervised Machine Learning techniques.

## Methodology
- Unsupervised model: Isolation Forest (anomaly detection without requiring
  labeled fraud examples upfront — relevant for real-world cases where new
  fraud typologies are unknown in advance).
- Supervised model: XGBoost trained on SMOTE-balanced data, providing a
  continuous risk score per transaction.
- Features: transaction amount, time, and PCA-derived components
  (to preserve banking data confidentiality).

## Key Results
- [Fill in with your actual figures: recall, precision for both models]
- Fraudulent transactions show [observed pattern on amount/time].

## Business Recommendations
1. Implement a real-time alert system on high-risk-scored transactions,
   with an adjustable threshold based on the client's risk appetite.
2. Prioritize manual review of high-amount, high-risk-score transactions
   (audit resource optimization).
3. Retrain the model periodically to adapt to evolving fraud typologies.

## Limitations
- Historical dataset (2013): a production deployment would require
  retraining on recent data.
- Trade-off between false positives (operational cost) and false negatives
  (financial risk) must be validated with the client's risk team.