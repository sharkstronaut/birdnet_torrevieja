import pandas as pd
import matplotlib.pyplot as plt

file_path = "temperature.csv"
df = pd.read_csv(file_path, parse_dates=['time'])

df_sampled = df.iloc[::300, :]
plt.figure(figsize=(10, 5))
plt.plot(df_sampled['time'], df_sampled['temperature'], marker='o', linestyle='-')
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Temperature over Time")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

