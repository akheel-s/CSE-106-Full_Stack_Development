import pandas as pd
import matplotlib.pyplot as plt

weather_data = pd.read_csv("weather_data.txt")
histogram = weather_data["actual_precipitation"].plot(kind = 'hist')
plt.xlabel("Precipiation Amount")
plt.ylabel("Number of Days")
plt.title("Actual Precipitation")

plt.show()