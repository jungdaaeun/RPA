import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

w = pd.read_csv('ch5-1.csv')
print(w, end="\n\n")
print(w.head(10), end="\n\n")

w_n = w.iloc[:, 1:5]
print(w_n, end='\n\n')
w_cor = w_n.corr(method = 'pearson')
print(w_cor, end='\n\n')

sns.pairplot(w_n)

plt.figure(figsize = (10,7))
sns.heatmap(w_cor, annot = True, cmap = 'Blues')
plt.show()