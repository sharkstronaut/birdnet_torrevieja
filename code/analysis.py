import os
import json
import matplotlib.pyplot as plt

# Directory containing all the .txt files
data_directory = 'birds_data'

# List all files in the directory
files = sorted([file for file in os.listdir(data_directory) if file.endswith(".txt")])

# Initialize a dictionary to store the bird counts over time for each location
bird_counts_per_location_over_time = {}

# Define predator birds
predator_birds = ["Apus apus", "Hirundo rustica", "Delichon urbicum", "Cecropis daurica",
                  "Caprimulgus ruficollis", "Muscicapa striata"]

# Iterate over the files and accumulate data
for file in files:
    month = file.split('_')[0]  # Get the month from the file name (assuming format "month_day_year.txt")
    
    with open(os.path.join(data_directory, file), "r", encoding="utf-8") as f:
        data = json.load(f)
    
    bird_counts_per_location = {}
    
    for entry in data["count"]:
        location = entry["location"]
        
        if location not in bird_counts_per_location:
            bird_counts_per_location[location] = 0  # Initialize count for the location
        
        for bird, count in entry["count"]:
            if bird in predator_birds:
                bird_counts_per_location[location] += count
    
    # Store the monthly counts per location
    for location, count in bird_counts_per_location.items():
        if location not in bird_counts_per_location_over_time:
            bird_counts_per_location_over_time[location] = {}
        bird_counts_per_location_over_time[location][month] = count

# Now you have bird counts for each location over time

# Plotting the time-series for each location
plt.figure(figsize=(10, 6))

for location, counts in bird_counts_per_location_over_time.items():
    months = list(counts.keys())
    count_values = list(counts.values())
    
    plt.plot(months, count_values, marker='o', label=location)

plt.xlabel("Month")
plt.ylabel("Predatory Bird Count")
plt.title("Predatory Bird Count Over Time for Different Locations")
plt.legend()
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()

