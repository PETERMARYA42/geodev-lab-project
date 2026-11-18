import geopandas as gpd

#Use geopandas to load my layer
stream = gpd.read_file("Processed/stream.gpkg")
print(stream.crs)

#Which UTM do my stream layer belongs?
est_crs = stream.estimate_utm_crs()
print("Suggested UTM is:", est_crs)

#Reproject to suggested UTM
change_to_crs = stream.to_crs(epsg=32736)
print(change_to_crs)

#Total length of my stream in km
length_stream = change_to_crs.length.sum() / 1_000_000
print("The total length of the stream is:", length_stream.round(2), "km")

stream.to_file("data/processed/stream.gpkg", layer="stream")