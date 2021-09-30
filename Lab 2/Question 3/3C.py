import pandas as pd

weather_data = pd.read_csv("weather_data.txt")
x = weather_data.loc[weather_data['actual_max_temp'] == weather_data['record_max_temp'],'date']

print(x)