"""
model_training.py

Aligned with Notebook 03_Modeling and 04_Evaluation.
Trains Isolation Forest, K-Means, and DBSCAN, applies PCA,
compares anomaly results, and saves model artifacts.
"""

import os
import json
import numpy as np
import pandas as pd
import joblib

from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, confusion_matrix


def train_isolation_forest(X, contamination=0.05, random_state=42):
    """Train Isolation Forest as the final anomaly detection model."""
    model = IsolationForest(
        n_estimators=200,
        contamination=contamination,
        random_state=random_state
    )

    model.fit(X)

    predictions = model.predict(X)
    anomaly_labels = np.where(predictions == -1, 1, 0)
    anomaly_scores = model.decision_function(X)

    return model, anomaly_labels, anomaly_scores


def train_kmeans_anomaly_model(X, n_clusters=2, random_state=42):
    """
    Train K-Means and flag the top 5 percent farthest points from
    cluster centers as anomalies.
    """
    model = KMeans(
        n_clusters=n_clusters,
        random_state=random_state,
        n_init=10
    )

    cluster_labels = model.fit_predict(X)

    distances = model.transform(X)
    min_distances = np.min(distances, axis=1)

    threshold = np.percentile(min_distances, 95)
    anomaly_labels = np.where(min_distances >= threshold, 1, 0)

    sil_score = silhouette_score(X, cluster_labels)

    return model, cluster_labels, min_distances, threshold, anomaly_labels, sil_score


def train_dbscan_anomaly_model(X, eps=0.8, min_samples=10):
    """Train DBSCAN and treat noise points (-1 label) as anomalies."""
    model = DBSCAN(eps=eps, min_samples=min_samples)

    cluster_labels = model.fit_predict(X)
    anomaly_labels = np.where(cluster_labels == -1, 1, 0)

    return model, cluster_labels, anomaly_labels


def apply_pca(X, n_components=2, random_state=42):
    """Apply PCA for 2D visualization of anomaly patterns."""
    pca = PCA(n_components=n_components, random_state=random_state)
    X_pca = pca.fit_transform(X)

    pca_df = pd.DataFrame(
        X_pca,
        columns=["PC1", "PC2"],
        index=X.index if hasattr(X, "index") else None
    )

    return pca, pca_df


def compare_model_outputs(results_df):
    """Create pairwise confusion matrices between model anomaly outputs."""
    return {
        "isolation_vs_kmeans": confusion_matrix(
            results_df["isolation_forest_anomaly"],
            results_df["kmeans_anomaly"]
        ).tolist(),
        "isolation_vs_dbscan": confusion_matrix(
            results_df["isolation_forest_anomaly"],
            results_df["dbscan_anomaly"]
        ).tolist(),
        "kmeans_vs_dbscan": confusion_matrix(
            results_df["kmeans_anomaly"],
            results_df["dbscan_anomaly"]
        ).tolist()
    }


def add_consensus_flags(results_df):
    """
    Add consensus anomaly flags:
    - detected_by_all_three
    - detected_by_at_least_two
    """
    results_df = results_df.copy()

    anomaly_sum = (
        results_df["isolation_forest_anomaly"]
        + results_df["kmeans_anomaly"]
        + results_df["dbscan_anomaly"]
    )

    results_df["detected_by_all_three"] = np.where(anomaly_sum == 3, 1, 0)
    results_df["detected_by_at_least_two"] = np.where(anomaly_sum >= 2, 1, 0)

    return results_df


def train_all_models(X):
    """Train all anomaly detection models and return notebook-aligned outputs."""
    iso_model, iso_anomaly, iso_scores = train_isolation_forest(X)

    kmeans_model, kmeans_clusters, kmeans_distances, kmeans_threshold, kmeans_anomaly, sil_score = (
        train_kmeans_anomaly_model(X)
    )

    dbscan_model, dbscan_clusters, dbscan_anomaly = train_dbscan_anomaly_model(X)

    pca_model, pca_df = apply_pca(X)

    results_df = pd.DataFrame(index=X.index if hasattr(X, "index") else None)
    results_df["isolation_forest_anomaly"] = iso_anomaly
    results_df["isolation_forest_score"] = iso_scores
    results_df["kmeans_cluster"] = kmeans_clusters
    results_df["kmeans_distance"] = kmeans_distances
    results_df["kmeans_anomaly"] = kmeans_anomaly
    results_df["dbscan_cluster"] = dbscan_clusters
    results_df["dbscan_anomaly"] = dbscan_anomaly
    results_df["PC1"] = pca_df["PC1"].values
    results_df["PC2"] = pca_df["PC2"].values

    results_df = add_consensus_flags(results_df)

    metrics = {
        "isolation_forest_anomaly_count": int(results_df["isolation_forest_anomaly"].sum()),
        "kmeans_anomaly_count": int(results_df["kmeans_anomaly"].sum()),
        "dbscan_anomaly_count": int(results_df["dbscan_anomaly"].sum()),
        "isolation_forest_anomaly_rate": float(results_df["isolation_forest_anomaly"].mean()),
        "kmeans_anomaly_rate": float(results_df["kmeans_anomaly"].mean()),
        "dbscan_anomaly_rate": float(results_df["dbscan_anomaly"].mean()),
        "kmeans_silhouette_score": float(sil_score),
        "kmeans_distance_threshold": float(kmeans_threshold),
        "pca_explained_variance_ratio": [float(x) for x in pca_model.explained_variance_ratio_],
        "model_agreement_matrices": compare_model_outputs(results_df),
        "detected_by_all_three_count": int(results_df["detected_by_all_three"].sum()),
        "detected_by_at_least_two_count": int(results_df["detected_by_at_least_two"].sum())
    }

    models = {
        "isolation_forest": iso_model,
        "kmeans": kmeans_model,
        "dbscan": dbscan_model,
        "pca": pca_model
    }

    return models, results_df, metrics


def save_artifacts(models, scaler, selector, label_encoders, selected_features, output_dir="models"):
    """Save model artifacts for reproducibility."""
    os.makedirs(output_dir, exist_ok=True)

    joblib.dump(models["isolation_forest"], os.path.join(output_dir, "isolation_forest_intrusion.pkl"))
    joblib.dump(models["kmeans"], os.path.join(output_dir, "kmeans_model.pkl"))
    joblib.dump(models["dbscan"], os.path.join(output_dir, "dbscan_model.pkl"))
    joblib.dump(models["pca"], os.path.join(output_dir, "pca.pkl"))
    joblib.dump(scaler, os.path.join(output_dir, "scaler.pkl"))
    joblib.dump(selector, os.path.join(output_dir, "variance_selector.pkl"))
    joblib.dump(label_encoders, os.path.join(output_dir, "label_encoders.pkl"))

    with open(os.path.join(output_dir, "selected_features.json"), "w") as f:
        json.dump(selected_features, f, indent=2)
