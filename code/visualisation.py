import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data from the CSV file
data = pd.read_csv("temperature_wind_rain_humidity_at_noon.csv")

# Step 2: Convert the 'time_temperature' column to datetime (you can use any of the time columns)
data["time_temperature"] = pd.to_datetime(data["time_temperature"])

# Step 3: Set the date as index (optional)
data.set_index("time_temperature", inplace=True)

# Step 4: Create a 2x2 grid of subplots (4 plots)
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Plot the Temperature data
axs[0, 0].plot(data.index, data["temperature"], marker='o', color="tab:blue")
axs[0, 0].set_title("Temperature Over Time")
axs[0, 0].set_xlabel("Date")
axs[0, 0].set_ylabel("Temperature (°C)")
axs[0, 0].grid(True)

# Plot the Wind data
axs[0, 1].plot(data.index, data["wind"], marker='s', color="tab:orange")
axs[0, 1].set_title("Wind Speed Over Time")
axs[0, 1].set_xlabel("Date")
axs[0, 1].set_ylabel("Wind (km/h)")
axs[0, 1].grid(True)

# Plot the Rain data
axs[1, 0].plot(data.index, data["rain"], marker='^', color="tab:green")
axs[1, 0].set_title("Rainfall Over Time")
axs[1, 0].set_xlabel("Date")
axs[1, 0].set_ylabel("Rain (mm)")
axs[1, 0].grid(True)

# Plot the Humidity data
axs[1, 1].plot(data.index, data["humidity"], marker='x', color="tab:red")
axs[1, 1].set_title("Humidity Over Time")
axs[1, 1].set_xlabel("Date")
axs[1, 1].set_ylabel("Humidity (%)")
axs[1, 1].grid(True)

# Step 5: Rotate the x-axis labels for better readability
for ax in axs.flat:
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

# Step 6: Adjust the layout to prevent overlap of subplots
plt.tight_layout()

# Step 7: Show the plot
plt.show()
