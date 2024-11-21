import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

w = pd.read_csv('ch5-1.csv')
w_n = w.iloc[:,1:5]

model_lm = smf.ols(formula = 'weight ~ food', data=w_n)

result_lm = model_lm.fit()

result_lm.summary()

print(result_lm.summary())

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

predicted_values = result_lm.predict()

mse = mean_squared_error(w_n['weight'], predicted_values)
mae = mean_absolute_error(w_n['weight'], predicted_values)
rmse = np.sqrt(mse)
r_squared = r2_score(w_n['weight'], predicted_values)

print("Mean Squared Error (MSE):", mse)
print("Mean Absolute Error (MAE):", mae)
print("Root Mean Squared Error (RMSE):", rmse)
print("R-squared:", r_squared)