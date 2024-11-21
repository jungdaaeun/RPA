import pandas as pd

w = pd.read_csv("ch7-1.csv")
print(w.head(), end='\n\n')

from sklearn.model_selection import train_test_split

x_data = w.iloc[:,0:2].values
y_data = w.iloc[:,2].values

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2)
print(len(pd.DataFrame(x_train)), len(pd.DataFrame(x_test)), end='\n\n')
print(len(pd.DataFrame(y_train)), len(pd.DataFrame(y_test)), end='\n\n')

from sklearn.neural_network import MLPRegressor
model_mlp = MLPRegressor().fit(x_train, y_train)

print(model_mlp.get_params(), end='\n\n')

y_pred_mlp = model_mlp.predict(x_test)
print(y_train, end='\n\n')
print(y_pred_mlp, end='\n\n')

df_x_test = pd.DataFrame(x_test, columns=['egg_weight','acc_food'])
df_y_pred = pd.DataFrame(y_pred_mlp, columns=['predict'])
df_y_test = pd.DataFrame(y_test , columns=['real'])
df = pd.concat([df_x_test , df_y_pred, df_y_pred], axis=1)
print(df, end='\n\n')

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
R2 = r2_score(y_test, y_pred_mlp)
print("R2 = ", R2, end='\n\n')