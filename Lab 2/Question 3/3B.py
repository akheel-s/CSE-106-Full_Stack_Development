import pandas as pd

weather_data = pd.read_csv("weather_data.txt")
july2014 = weather_data[weather_data['date'].str.contains('2014-7')]
average = july2014['actual_max_temp'].mean()

print(average)