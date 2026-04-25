"""
feature_engineering.py

Aligned with Notebook 02_Feature_Engineering.
Encodes categorical features, creates ratio-based cybersecurity features,
scales data, and applies VarianceThreshold feature selection.
"""

import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.feature_selection import VarianceThreshold


def encode_categorical_features(df):
    """Encode categorical variables using LabelEncoder."""
    df = df.copy()
    label_encoders = {}

    categorical_cols = df.select_dtypes(exclude=[np.number]).columns

    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        label_encoders[col] = le

    return df, label_encoders


def create_engineered_features(df):
    """
    Create domain-based ratio features used in the notebook:
    - login_failure_ratio
    - byte_ratio
    - service_to_host_ratio
    - dst_host_service_ratio
    """
    df = df.copy()

    if "num_failed_logins" in df.columns and "count" in df.columns:
        df["login_failure_ratio"] = df["num_failed_logins"] / (df["count"] + 1)

    if "src_bytes" in df.columns and "dst_bytes" in df.columns:
        df["byte_ratio"] = df["src_bytes"] / (df["dst_bytes"] + 1)

    if "srv_count" in df.columns and "count" in df.columns:
        df["service_to_host_ratio"] = df["srv_count"] / (df["count"] + 1)

    if "dst_host_srv_count" in df.columns and "dst_host_count" in df.columns:
        df["dst_host_service_ratio"] = df["dst_host_srv_count"] / (df["dst_host_count"] + 1)

    return df


def scale_features(df):
    """Apply StandardScaler so all features use a comparable scale."""
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df)

    X_scaled_df = pd.DataFrame(
        X_scaled,
        columns=df.columns,
        index=df.index
    )

    return X_scaled_df, scaler


def apply_feature_selection(X_scaled_df, threshold=0.01):
    """
    Apply VarianceThreshold as the formal feature selection step.
    Low-variance features are removed before modeling.
    """
    selector = VarianceThreshold(threshold=threshold)
    X_selected = selector.fit_transform(X_scaled_df)

    selected_features = X_scaled_df.columns[selector.get_support()].tolist()

    X_selected_df = pd.DataFrame(
        X_selected,
        columns=selected_features,
        index=X_scaled_df.index
    )

    return X_selected_df, selector, selected_features


def prepare_features(df):
    """Full feature engineering pipeline aligned with the notebook."""
    df_encoded, label_encoders = encode_categorical_features(df)
    df_engineered = create_engineered_features(df_encoded)
    X_scaled_df, scaler = scale_features(df_engineered)
    X_selected_df, selector, selected_features = apply_feature_selection(X_scaled_df)

    return X_selected_df, scaler, selector, label_encoders, selected_features, df_engineered
