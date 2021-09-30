import pandas as pd

weather_data = pd.read_csv("weather_data.txt")
x = weather_data.sort_values(by = "actual_precipitation")
date = x["date"][0]

print(date)