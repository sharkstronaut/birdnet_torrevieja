import json
import csv
from datetime import datetime

with open('humidity.json', 'r') as file:
    data = json.load(file)

series = data.get("series", {})

temperatura_data = series.get("humedad", {})

with open('humidity.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['time', 'humidity'])
    for sensor_id, readings in temperatura_data.items():
        for reading in readings:
            timestamp, value = reading
            time_str = datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')
            csvwriter.writerow([time_str, value])