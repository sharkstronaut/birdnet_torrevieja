import pandas as pd

# Step 1: Load the temperature, wind, rain, and humidity data from their respective CSV files
temperature_data = pd.read_csv("temperature.csv")
wind_data = pd.read_csv("wind.csv")
rain_data = pd.read_csv("rain.csv")
humidity_data = pd.read_csv("humidity.csv")

# Step 2: Convert the 'time' columns to datetime
temperature_data["time"] = pd.to_datetime(temperature_data["time"])
wind_data["time"] = pd.to_datetime(wind_data["time"])
rain_data["time"] = pd.to_datetime(rain_data["time"])
humidity_data["time"] = pd.to_datetime(humidity_data["time"])

# Step 3: Extract date, hour, and minute for all datasets
temperature_data["Date"] = temperature_data["time"].dt.date  # Extract only the date
temperature_data["Hour"] = temperature_data["time"].dt.hour  # Extract the hour
temperature_data["Minute"] = temperature_data["time"].dt.minute  # Extract the minute

wind_data["Date"] = wind_data["time"].dt.date  # Extract only the date
wind_data["Hour"] = wind_data["time"].dt.hour  # Extract the hour
wind_data["Minute"] = wind_data["time"].dt.minute  # Extract the minute

rain_data["Date"] = rain_data["time"].dt.date  # Extract only the date
rain_data["Hour"] = rain_data["time"].dt.hour  # Extract the hour
rain_data["Minute"] = rain_data["time"].dt.minute  # Extract the minute

humidity_data["Date"] = humidity_data["time"].dt.date  # Extract only the date
humidity_data["Hour"] = humidity_data["time"].dt.hour  # Extract the hour
humidity_data["Minute"] = humidity_data["time"].dt.minute  # Extract the minute

# Step 4: Filter all datasets for only the readings at 12:00 PM (noon)
temperature_noon = temperature_data[(temperature_data["Hour"] == 12) & (temperature_data["Minute"] == 0)]
wind_noon = wind_data[(wind_data["Hour"] == 12) & (wind_data["Minute"] == 0)]
rain_noon = rain_data[(rain_data["Hour"] == 12) & (rain_data["Minute"] == 0)]
humidity_noon = humidity_data[(humidity_data["Hour"] == 12) & (humidity_data["Minute"] == 0)]

# Step 5: Merge the temperature, wind, rain, and humidity data on the Date column
merged_data = pd.merge(temperature_noon[["time", "temperature", "Date"]],
                       wind_noon[["time", "wind", "Date"]],
                       on="Date", suffixes=("_temperature", "_wind"))

merged_data = pd.merge(merged_data, rain_noon[["time", "rain", "Date"]],
                       on="Date", suffixes=("", "_rain"))

merged_data = pd.merge(merged_data, humidity_noon[["time", "humidity", "Date"]],
                       on="Date", suffixes=("", "_humidity"))

# Step 6: Remove the Date column (optional) and keep only the time, temperature, wind, rain, and humidity columns
final_data = merged_data.drop(columns=["Date"])

# Step 7: Save the resulting data to a new CSV file
final_data.to_csv("temperature_wind_rain_humidity_at_noon.csv", index=False)

# Step 8: Show the resulting DataFrame (Optional)
print(final_data)
