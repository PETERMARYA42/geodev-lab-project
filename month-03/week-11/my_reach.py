import geopandas as gpd

boundary = gpd.read_file("processed/Chamwino_wards_boundary_UTM36S.gpkg",layer="Chamwino_wards_boundary_UTM36S",)
school = gpd.read_file("Processed/schoolS_UTM36S.gpkg")

centres = boundary[["NAME_3", "geometry"]].copy()
centres["geometry"] = boundary.centroid

nearest = gpd.sjoin_nearest(
    centres, school[["name", "geometry"]], how="left", distance_col="distance_m"
)
nearest["distance_km"] = (nearest["distance_m"] / 1000).round(2)

print(nearest[["NAME_3", "name", "distance_km"]])