import pandas as pd
import matplotlib.pyplot as plt

# Update the file path to your .txt file
file_path = "insecticides_per_month.txt"

# Read the .txt file with semicolon delimiter
df = pd.read_csv(file_path, delimiter=';', parse_dates=['Time'])

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(df['Time'], df['UnidadesVenta'], marker='o', linestyle='-')
plt.xlabel("Time")
plt.ylabel("Unidades Venta")
plt.title("Unidades Venta over Time")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()