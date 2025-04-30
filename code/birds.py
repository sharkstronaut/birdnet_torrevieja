import matplotlib.pyplot as plt
import json

with open("birds_data/24_6_7.txt", "r", encoding="utf-8") as file:
    data = json.load(file)

bird_counts_per_location = {}

predator_birds = ["Apus apus", "Hirundo rustica", 
                  "Delichon urbicum", "Cecropis daurica",
                  "Caprimulgus ruficollis", "Muscicapa striata"
                  ]

for entry in data["count"]:
    location = entry["location"]
    
    if location not in bird_counts_per_location:
        bird_counts_per_location[location] = {}

    for bird, count in entry["count"]:
        if bird in bird_counts_per_location[location]:
            bird_counts_per_location[location][bird] += count
        else:
            bird_counts_per_location[location][bird] = count

data = {}
for location, birds in bird_counts_per_location.items():
    i = 0
    for bird, count in birds.items():
        if bird in predator_birds:
            i += 1
    print(f"Location: {location} : {i}")
    data[location] = i


locations = list(data.keys())
counts = list(data.values())

plt.figure(figsize=(10, 5))
plt.bar(locations, counts, color="skyblue")

plt.xlabel("Location")
plt.ylabel("Predatory Bird Count")
plt.title("Predatory Bird Count per Location")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()