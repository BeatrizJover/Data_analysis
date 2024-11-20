import pandas as pd
from shapely.geometry import Point
import geopandas as gpd
import matplotlib.pyplot as plt
import os


# Load the CSV into a DataFrame
file_path = "/home/betty/Desktop/Data_analysis/csv-data/cleaned_dataset_analysis.csv" 
df = pd.read_csv(file_path)
df_2 = pd.read_csv('/home/betty/Desktop/Data_analysis/belgian-cities-geocoded.csv')

print(df.columns)
# Disable scientific notation
pd.set_option('display.float_format', '{:.2f}'.format)
print(df["Price"].describe()) # Description of the dataframe
ave_price = df['Price'].mean()
med_price = df['Price'].median()
print(ave_price)
print(med_price)

# Group by Province and Subtype of Property, calculate average price
grouped = df.groupby(['Province','Zip Code', 'Subtype of Property'])['Price'].mean().reset_index()
print(grouped)

print(grouped['Zip Code'].dtype)
print(df_2['postal'].dtype)
grouped['Zip Code'] = grouped['Zip Code'].astype(str)
df_2['postal'] = df_2['postal'].astype(str)
df_2_filtered = df_2[['postal', 'lat', 'lng']]

# Merge on mismatched column names ('Zip Code' and 'postal')
merged_df = pd.merge(grouped, df_2_filtered, left_on='Zip Code', right_on='postal', how='left')

# Drop the 'postal' column if not needed after the merge
merged_df.drop(columns=['postal'], inplace=True)

print(merged_df)

merged_df.dropna(subset=['lat', 'lng'], inplace=True)
print(merged_df.isna().sum())



# Create a geometry column from latitude and longitude
geometry = [Point(xy) for xy in zip(merged_df['lng'], merged_df['lat'])]

# Convert the DataFrame to a GeoDataFrame
gdf = gpd.GeoDataFrame(merged_df, geometry=geometry)

# Set the Coordinate Reference System (CRS) to WGS84 (EPSG:4326), commonly used for GeoJSON
gdf.set_crs(epsg=4326, inplace=True)

gdf.to_file("output.geojson", driver="GeoJSON")

# Suponiendo que el archivo se llama 'mi_archivo.txt'
archivo = "output.geojson"

# Obtener la ruta completa del archivo
path_file = os.path.abspath(archivo)
print(path_file)



# Load your GeoDataFrame (replace the path with your actual file)
gdf = gpd.read_file('/home/betty/Becode_training_path/Projects/Data_analysis/csv-data/output.geojson')

# Plot the house prices on the map, coloring by price
ax = gdf.plot(column='Price', cmap='coolwarm', legend=True, figsize=(10, 10))

# Set the title for the map
ax.set_title('House Prices in Region')

# Display the plot
plt.show()





