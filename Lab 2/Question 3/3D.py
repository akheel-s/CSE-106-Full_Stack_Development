import pandas as pd

weather_data = pd.read_csv("weather_data.txt")
x = weather_data.loc[weather_data['date'].str.contains('2014-10'), 'actual_precipitation']

print(x.sum())