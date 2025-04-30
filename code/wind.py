import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "wind.csv"  # Update with the actual file path
df = pd.read_csv(file_path, parse_dates=['time'])

# Resample to get one data point every 12 hours
df_resampled = df.set_index('time').resample('12H').first().reset_index()

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(df_resampled['time'], df_resampled['wind'], marker='o', linestyle='-')

# Formatting
plt.xlabel("Time")
plt.ylabel("Wind Speed")
plt.title("Wind Speed Over Time (Every 12 Hours)")
plt.xticks(rotation=45)
plt.grid(True)

# Show the plot
plt.show()
