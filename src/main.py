"""
main.py

One-command pipeline for the capstone project.

Recommended command:
python src/main.py --data data/raw/Train_data.csv --output outputs --models models
"""

import argparse
import os
import json

from data_preprocessing import preprocess_data
from feature_engineering import prepare_features
from model_training import train_all_models, save_artifacts


def main(data_path, output_dir, models_dir):
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(models_dir, exist_ok=True)

    # Step 1-3: Load, clean, engineer, scale, and select features
    df_clean = preprocess_data(data_path)
    X_selected, scaler, selector, label_encoders, selected_features, df_engineered = prepare_features(df_clean)

    # Step 4: Train and compare models
    models, results_df, metrics = train_all_models(X_selected)

    # Save outputs
    df_engineered.to_csv(os.path.join(output_dir, "processed_features.csv"), index=False)
    results_df.to_csv(os.path.join(output_dir, "model_predictions_and_scores.csv"), index=False)

    with open(os.path.join(output_dir, "evaluation_metrics.json"), "w") as f:
        json.dump(metrics, f, indent=2)

    # Save models and preprocessing artifacts
    save_artifacts(
        models=models,
        scaler=scaler,
        selector=selector,
        label_encoders=label_encoders,
        selected_features=selected_features,
        output_dir=models_dir
    )

    print("Pipeline completed successfully.")
    print(f"Processed files saved to: {output_dir}")
    print(f"Model files saved to: {models_dir}")
    print("Summary Metrics:")
    for key, value in metrics.items():
        if key != "model_agreement_matrices":
            print(f"- {key}: {value}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run cybersecurity anomaly detection capstone pipeline.")
    parser.add_argument("--data", required=True, help="Path to Train_data.csv")
    parser.add_argument("--output", default="outputs", help="Folder for output CSV/JSON files")
    parser.add_argument("--models", default="models", help="Folder for saved .pkl model files")

    args = parser.parse_args()
    main(data_path=args.data, output_dir=args.output, models_dir=args.models)
