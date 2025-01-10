# Enhanced Bankruptcy Prediction Using ARIMA-Neural Network Model

## Overview
Traditional models for bankruptcy prediction, such as Altman's Z-score and logistic regression, often fail to account for non-linear patterns in financial data. This project proposes a hybrid model combining ARIMA and Neural Networks to improve prediction accuracy and robustness.

## Objectives
- Develop a hybrid ARIMA-Neural Network model for bankruptcy prediction.
- Compare performance against traditional models using metrics such as RMSE and MAPE.
- Provide insights for financial risk management.

## Key Features
- **Time Series Analysis**: ARIMA for capturing linear trends and seasonality.
- **Neural Networks**: Modeling complex, non-linear dependencies.
- **Hybrid Approach**: Improved accuracy and adaptability.

## Dataset
The dataset includes financial metrics such as profit margins, debt ratios, and historical bankruptcy data.

## Evaluation Metrics
- Mean Absolute Error (MAE)
- Mean Absolute Percentage Error (MAPE)
- Root Mean Square Error (RMSE)

## Results Summary
| Model               | MAE  | MAPE  |
|---------------------|------|-------|
| ARIMA               | 6.23 | 12.45%|
| Combined ARIMA + NN | 7.45 | 15.67%|

## Repository Structure
- `data/` : Contains datasets used for the project.
- `models/` : Code for ARIMA, Neural Networks, and hybrid model.
- `results/` : Evaluation metrics and visualization outputs.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/espirado/bankruptcy-prediction-.git
