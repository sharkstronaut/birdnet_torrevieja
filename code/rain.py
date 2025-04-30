import pandas as pd
import matplotlib.pyplot as plt

file_path = "rain.csv"
df = pd.read_csv(file_path, parse_dates=['time'])

df_resampled = df.set_index('time').resample('12H').first().reset_index()


plt.figure(figsize=(10, 5))
plt.plot(df_resampled['time'], df_resampled['rain'], marker='o', linestyle='-')

plt.xlabel("Time")
plt.ylabel("Rain (%)")
plt.title("Rain Over Time (Every 12 Hours)")
plt.xticks(rotation=45)
plt.grid(True)

plt.show()
