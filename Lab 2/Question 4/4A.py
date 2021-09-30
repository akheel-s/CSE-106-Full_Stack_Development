import pandas as pd
import matplotlib.pyplot as plt

weather_data = pd.read_csv("weather_data.txt")
min = weather_data["actual_min_temp"]
max = weather_data["actual_max_temp"]

plt.plot(min, color = "blue", label='Actual Minimum Temperature')
plt.plot(max, color = "red", label='Actual Maximum Temperature')
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.title("Day vs. Temperature")


# line_plot = weather_data["actual_min_temp", "actual_max_temp"].plot.line()
plt.legend()
plt.show()