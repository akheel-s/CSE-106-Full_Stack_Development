import pandas as pd

weather_data = pd.read_csv("weather_data.txt")
x = weather_data.loc[(weather_data['actual_max_temp'] > 90) & (weather_data['actual_min_temp'] < 60),'date']

print(x)