import pandas as pd
import matplotlib.pyplot as plt

def load_excel(file_path):
    # Load the Excel file
    df = pd.read_excel(file_path, usecols=["NombreMerca", "Familia", "Subfamilia", "TipoDatoVentas", "Periodo", "Año", "Mes", "UnidadesVenta"])
    return df  # Return the DataFrame directly

def plot_sales_per_month(df):
    # Group data by NombreMerca and sort by Año and Mes
    grouped = df.groupby("NombreMerca")
    
    for nombre_merca, group in grouped:
        # Sort by year and month
        group = group.sort_values(by=["Año", "Mes"])
        
        # Create a time axis (combining Año and Mes)
        time_axis = group["Año"].astype(str) + "-" + group["Mes"].astype(str).str.zfill(2)
        
        # Plot sales per month
        plt.plot(time_axis, group["UnidadesVenta"], marker='o', label=nombre_merca)
    
    # Add labels and legend
    plt.xlabel("Time (Year-Month)")
    plt.ylabel("Sales (UnidadesVenta)")
    plt.title("Sales per Month for Each NombreMerca")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_sales_for_nombre_merca(df, nombre_merca):
    # Filter the DataFrame for the specific NombreMerca
    filtered_df = df[df["NombreMerca"] == nombre_merca]
    
    # Sort by year and month
    filtered_df = filtered_df.sort_values(by=["Año", "Mes"])
    
    # Create a time axis (combining Año and Mes)
    time_axis = filtered_df["Año"].astype(str) + "-" + filtered_df["Mes"].astype(str).str.zfill(2)
    
    # Plot sales per month
    plt.plot(time_axis, filtered_df["UnidadesVenta"], marker='o', label=nombre_merca)
    
    # Add labels and legend
    plt.xlabel("Time (Year-Month)")
    plt.ylabel("Sales (UnidadesVenta)")
    plt.title(f"Sales per Month for {nombre_merca}")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_total_sales_per_month(df):
    # Group data by Año and Mes and calculate the sum of UnidadesVenta
    grouped = df.groupby(["Año", "Mes"])["UnidadesVenta"].sum().reset_index()

    # Create a time axis (combining Año and Mes)
    grouped["Time"] = grouped["Año"].astype(str) + "-" + grouped["Mes"].astype(str).str.zfill(2)

    # Plot total sales per month
    plt.plot(grouped["Time"], grouped["UnidadesVenta"], marker='o', label="Total Sales")

    # Add labels and legend
    plt.xlabel("Time (Year-Month)")
    plt.ylabel("Total Sales (UnidadesVenta)")
    plt.title("Total Sales per Month")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

    return grouped  # Return the grouped DataFrame for export

def export_total_sales_to_txt(grouped, output_file):
    # Export the grouped DataFrame to a .txt file with a semicolon delimiter
    grouped.to_csv(output_file, sep=';', index=False, encoding='utf-8')
    print(f"Total sales per month exported to {output_file}")

def main():
    file_path = 'Ventas mensuales voladores.xlsx'
    df = load_excel(file_path)
    # plot_sales_per_month(df)
    # for nombre_merca in df["NombreMerca"].unique():
    #     #print(f"Plotting sales for {nombre_merca}")
    #     plot_sales_for_nombre_merca(df, nombre_merca)
    grouped = plot_total_sales_per_month(df)
    export_total_sales_to_txt(grouped, 'Insecticides_per_month.txt')

if __name__ == "__main__":
    main()