"""
data_preprocessing.py

Aligned with Notebook 01_EDA / preprocessing section.
Handles loading, missing values, duplicates, and IQR-based outlier capping.
"""

import pandas as pd
import numpy as np


def load_data(file_path):
    """Load the raw training dataset."""
    return pd.read_csv(file_path)


def basic_data_overview(df):
    """Return basic dataset information used during EDA."""
    return {
        "shape": df.shape,
        "columns": list(df.columns),
        "missing_values": df.isnull().sum(),
        "duplicates": int(df.duplicated().sum()),
        "data_types": df.dtypes
    }


def handle_missing_values(df):
    """
    Handle missing values:
    - Numeric columns: median imputation
    - Categorical columns: mode imputation
    """
    df = df.copy()

    numeric_cols = df.select_dtypes(include=[np.number]).columns
    categorical_cols = df.select_dtypes(exclude=[np.number]).columns

    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    for col in categorical_cols:
        if not df[col].mode().empty:
            df[col] = df[col].fillna(df[col].mode()[0])

    return df


def remove_duplicates(df):
    """Remove duplicate records."""
    return df.drop_duplicates().reset_index(drop=True)


def cap_outliers_iqr(df):
    """
    Apply IQR-based capping to numeric features.
    This reduces extreme values without removing records.
    """
    df = df.copy()
    numeric_cols = df.select_dtypes(include=[np.number]).columns

    for col in numeric_cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        df[col] = np.clip(df[col], lower_bound, upper_bound)

    return df


def preprocess_data(file_path):
    """Full preprocessing pipeline aligned with the notebook."""
    df = load_data(file_path)
    df = handle_missing_values(df)
    df = remove_duplicates(df)
    df = cap_outliers_iqr(df)
    return df
