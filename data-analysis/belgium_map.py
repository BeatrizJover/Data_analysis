import folium
from folium.plugins import MarkerCluster
import geopandas as gpd

# Crear un mapa base centrado en Bélgica (latitud y longitud aproximada del centro de Bélgica)
m = folium.Map(location=[50.8503, 4.3517], zoom_start=7, tiles='OpenStreetMap')

# Si deseas agrupar los puntos en clusters
marker_cluster = MarkerCluster().add_to(m)



# Load your GeoDataFrame (replace the path with your actual file)
gdf = gpd.read_file('/home/betty/Becode_training_path/Projects/Data_analysis/csv-data/output.geojson')

# Añadir los puntos al mapa
for idx, row in gdf.iterrows():
    folium.Marker([row['lat'], row['lng']], popup=f"Price: {row['Price']}, Type: {row['Subtype of Property']}").add_to(marker_cluster)

# Guardar el mapa en un archivo HTML
m.save("belgium_map.html")