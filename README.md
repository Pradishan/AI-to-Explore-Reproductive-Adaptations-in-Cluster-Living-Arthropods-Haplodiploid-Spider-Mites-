# AI Models for Spider-Mite (exploring population dynamics) Research

This repository contains data analysis, preprocessing, machine-learning, time-series forecasting, synthetic-data generation, and computer-vision experiments for spider-mite research.

## Getting started

Create a Python virtual environment and install the project dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

The work is primarily organised as Jupyter notebooks. Launch Jupyter from the repository root:

```powershell
jupyter notebook
```

## Project structure

- `data/` — source, processed, and synthetic datasets.
- `Data analysis and preprossing/` — exploratory data analysis notebooks and visualisations.
- `models/` — experiments for prediction, forecasting, synthetic data, and image analysis.
- `src/` — reusable Python utilities, including data preprocessing.
- `requirements.txt` — Python packages required by the project.

## Main areas of work

- Exploratory data analysis and preprocessing
- Prediction models, including XGBoost, Random Forest, LightGBM, CatBoost, and MLP
- Time-series forecasting with SARIMA and Bi-LSTM approaches
- Synthetic-data generation with bootstrap, SMOTE, VAE, GAN, and diffusion methods
- Computer-vision experiments with YOLO

## Data preprocessing

The `src/data_preprocessor.py` module provides a helper that converts the observation and introduction date columns to datetime values:

```python
import pandas as pd
from src.data_preprocessor import preprocess_data

data = pd.read_csv("data/data.csv")
data = preprocess_data(data)
```

## Notes

Run notebook cells in order, and start them from the repository root so relative paths resolve correctly. Some experiments may require additional notebook-specific configuration or data preparation.
