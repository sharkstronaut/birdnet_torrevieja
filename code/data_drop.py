import pandas as pd

# Step 1: Load the data from the CSV file
data = pd.read_csv("temperature_wind_rain_humidity_at_noon.csv")

# Step 2: Drop the extra 'time_something' columns
data.drop(columns=['time_temperature', 'time_wind', 'time_humidity'], inplace=True)

# Step 3: Ensure that 'time' column is in datetime format
#data["time"] = pd.to_datetime(data["time"])

# Step 4: Now data will only have a single time column with relevant information
# Display the cleaned data
print(data)

# Step 5: Save the cleaned data to a new CSV (optional)
data.to_csv("cleaned_data.txt", sep=",", index=False)
