import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point


df1 = pd.read_csv("C:\\FIA-Data\\FIA_data\\1_COND_selected_all_USA_drought_bilinear_interpolation_combine_new_delete_blank_2001_2020.csv")

try1 = df1['num_of_slow_drought']
summary = df1.groupby(['LAT', 'LON'])['num_of_slow_drought'].sum().reset_index()
summary.to_csv("C:\\FIA-Data\\FIA_data\\1_COND_selected_all_USA_drought_bilinear_interpolation_combine_new_delete_blank_2001_2020_num_flash.csv", index=False)



# Load the shapefile
shape = gpd.read_file("C:\\Users\\zhijiel\\OneDrive\\Shapefile\\US_continental\\ne_110m_admin_1_states_provinces.shp")

# Load the DataFrame
df2 = pd.read_csv("C:\\FIA-Data\\FIA_data\\1_COND_selected_all_USA_drought_bilinear_interpolation_combine_new_delete_blank_2001_2020_num_flash.csv")

# Convert df2 to a GeoDataFrame
gdf = gpd.GeoDataFrame(df2, geometry=gpd.points_from_xy(df2.LON, df2.LAT))

# Ensure the GeoDataFrame and shapefile have the same CRS
gdf.crs = shape.crs



# Plot the shapefile
fig, ax = plt.subplots(figsize=(10, 10))
shape.plot(ax=ax, color='white', edgecolor='black')


# Plot the scatter distribution on top of the shapefile
gdf.plot(ax=ax, markersize=2, column='num_of_slow_drought', legend=True, cmap='coolwarm', alpha=0.2, marker='s', vmin=0, vmax=5)

# Set aspect ratio to 'equal'
ax.set_aspect('equal')

# Add a title
plt.title('Slow Drought Frequencies in the USA (2001_2020)', fontsize=20, loc='left')

# Add a rectangle to fill the area outside the shapefile
minx, miny, maxx, maxy = shape.total_bounds
rect = plt.Rectangle((minx, miny), maxx - minx, maxy - miny, fill=True, color='grey', alpha=0.5, zorder=0)
ax.add_patch(rect)

# plt.savefig("C:\\FIA-Data\\FIA_data\\1_COND_selected_all_USA_drought_bilinear_interpolation_combine_new_delete_blank_1981_2000_num.png", dpi=600)

plt.show()
