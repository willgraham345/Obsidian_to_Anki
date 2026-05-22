---
summary:
headings:
type:
date created: Tuesday, October 28th 2025, 12:25:27 pm
date modified: Tuesday, October 28th 2025, 12:25:59 pm
template:
template-version:
---

# Notes:
- SAGE = Automated anomaly detection in satellite telemetry through machine learning.
- Running as a standalone service within the telemetry data in satellite ground station


- Kafka broker?

Extended Isolation forest (EIF) model
- Unsupervised machine learning model
- A huge decision tree worth of data
- `sklearn.IsolationForest`

KNN model

Subspace PCA (SubPCA) model
- You have a data matrix
- You're trying to use LVD (decomposition)
	- Trying to solve for eigenvalues on matrix, put them in diagonal matrix (after ranking them), grab the 5 highest eigenvectors, and from there reduce the number of dimensions you have in your datasets to find an anomaly.
- They used 16 threads on key columns, sliding windows for temporal patterns
- Applies the `pyod.PCA` with variance
- Mapping window scores
- This one is sensitive to temporal anomalizes in individual telemetry variables.
- Sudden change in attitude of a satellite would be good at finding this.


Preprocessing and Exploratory Data Analysis
- You have to preprocess your data correctly before putting it into your model.

Performance
- Precision, Recall, F1, ROC-AUC, PR-AUC
- Ways the model evaluates its performance
- Once you split your data, you may have an "unfortunate split"