import geopandas as gpd

boundary = gpd.read_file("processed/Chamwino_wards_boundary_UTM36S.gpkg")
school = gpd.read_file("Processed/schoolS_UTM36S.gpkg")

#Spatial join (points inside polygons)
joined = gpd.sjoin(school, boundary, how="inner", predicate="within")

#Group by the ward column ('NAME_3') and count
counts = joined.groupby("NAME_3").size().rename("school_count").reset_index()

#Merge back to boundary using 'NAME_3'
boundary = boundary.merge(counts, on="NAME_3", how="left")
boundary["school_count"] = boundary["school_count"].fillna(0).astype(int)

print(boundary[["NAME_3", "school_count"]].head())