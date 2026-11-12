import geopandas as gpd

print(gpd.list_layers("Processed/roads_UTM36S.gpkg"))
my_roads = gpd.read_file("Processed/roads_UTM36S.gpkg", layer="roads_UTM36S")

print(my_roads.head(3))
print("Rows and columns:", my_roads.shape)
print("Geometry:", my_roads.geometry.type)
print("CRS:", my_roads.crs)
print("Bounds:", my_roads.total_bounds)