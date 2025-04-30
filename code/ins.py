import pandas as pd

# Load the dataset
file_path = "Insecticides_per_month.txt"  # Replace with your file path
df = pd.read_csv(file_path, delimiter=';')

# Group by 'Mes' (month) and sum 'UnidadesVenta' across all years
df_grouped = df.groupby('Mes', as_index=False)['UnidadesVenta'].sum()

# Sort by month for better readability
df_grouped = df_grouped.sort_values('Mes')

# Save the result to a .txt file
output_file = "Insecticides_per_month_grouped.txt"  # Replace with your desired output file path
df_grouped.to_csv(output_file, sep=';', index=False)

# Display the result
print(df_grouped)

# Optional: Plot the result
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.bar(df_grouped['Mes'], df_grouped['UnidadesVenta'], color='skyblue')
plt.xlabel("Month")
plt.ylabel("Total Units Sold")
plt.title("Total Units Sold by Month Across All Years")
plt.xticks(range(1, 13))  # Ensure months are displayed as 1-12
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()