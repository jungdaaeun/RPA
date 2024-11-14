import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

w = pd.read_csv('ch5-1.csv')
w_n = w.iloc[:,1:5]

model_lm = smf.ols(formula = 'weight ~ food', data = w_n)
result_lm = model_lm.fit()
result_lm.summary()

print(result_lm.summary())

plt.figure(figsize = (10,7))
plt.scatter(w.food, w.weight, alpha = .5)
plt.plot(w.food, w.food*4.6684 + 78.1551, color = 'red')
plt.text(13, 132, 'weight = 4.6684food + 78.1551', fontsize = 12)
plt.title('Scatter Plot')
plt.xlabel('food')
plt.ylabel('weight')
plt.show()