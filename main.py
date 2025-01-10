import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
import os

# Create outputs directory if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Simulate financial dataset (for demo purposes)
np.random.seed(42)
data = np.cumsum(np.random.randn(200))  # Mimic financial time series
df = pd.DataFrame({'value': data})

# Split into train and test sets
train, test = train_test_split(df['value'], test_size=0.2, shuffle=False)

# ARIMA model
arima_model = ARIMA(train, order=(1, 1, 1))
arima_fit = arima_model.fit()
arima_forecast = arima_fit.forecast(steps=len(test))

# Plot ARIMA forecast
plt.figure(figsize=(10, 6))
plt.plot(train.index, train, label='Train')
plt.plot(test.index, test, label='Test')
plt.plot(test.index, arima_forecast, label='ARIMA Forecast')
plt.legend()
plt.title('ARIMA Model Forecast')
plt.savefig('outputs/arima_forecast.png')

# Prepare input for Neural Network (using ARIMA residuals)
residuals = train - arima_fit.predict()
X = np.array(residuals).reshape(-1, 1)
y = train[1:]

# Neural Network
nn_model = MLPRegressor(hidden_layer_sizes=(10, 5), max_iter=500, random_state=42)
nn_model.fit(X[:-1], y)

# Prediction using NN on ARIMA residuals
nn_forecast = nn_model.predict(np.array(residuals[-len(test):]).reshape(-1, 1))

# Combined prediction (ARIMA + NN)
final_forecast = arima_forecast + nn_forecast

# Evaluation
rmse = np.sqrt(mean_squared_error(test, final_forecast))
print(f"RMSE: {rmse}")

# Save RMSE to a text file
with open('outputs/evaluation.txt', 'w') as f:
    f.write(f"RMSE: {rmse}\n")

# Plot combined forecast
plt.figure(figsize=(10, 6))
plt.plot(test.index, test, label='Actual')
plt.plot(test.index, final_forecast, label='Combined ARIMA + NN Forecast')
plt.legend()
plt.title('Combined ARIMA + Neural Network Model')
plt.savefig('outputs/combined_forecast.png')

# Save predictions to CSV
output_df = pd.DataFrame({'Actual': test.values, 'ARIMA_Forecast': arima_forecast, 'Combined_Forecast': final_forecast})
output_df.to_csv('outputs/predictions.csv', index=False)
