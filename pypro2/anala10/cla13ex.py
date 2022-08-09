import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("bike_dataset.csv")
pd.set_option('display.max_columns', None)
print(df.head(3), df.shape) # (10886, 12)
print(df.columns)
print(df.corr())

x = df[['registered', 'casual', 'humidity', 'atemp' ,'temp']].values
y = df['count'].values
print(x[:3])
print(y[:3])
print()

# 실습2 : RandomForestRegressor
model2 = RandomForestRegressor(n_estimators=1000, criterion='squared_error').fit(x,y)
print('예측값:', model2.predict(x)[:5])
print('실제값:', y[:5])
print('결정계수:', r2_score(y, model2.predict(x)))









