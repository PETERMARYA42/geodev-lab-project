import geopandas as gpd
from shapely.validation import explain_validity

boundary = gpd.read_file("processed/Chamwino_wards_boundary_UTM36S.gpkg",layer="Chamwino_wards_boundary_UTM36S",)
print(boundary.is_valid)
print(boundary.geom_type.iloc[0])