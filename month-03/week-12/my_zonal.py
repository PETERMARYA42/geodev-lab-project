import geopandas as gpd
import numpy as np
import rasterio
from rasterio.mask import mask

with rasterio.open("chamwinoDEM.tif") as src:
    wards = gpd.read_file("Processed/Chamwino_wards_boundary_UTM36S.gpkg").to_crs(src.crs)
    means = []
    for geom in wards.geometry:
        cells, _ = mask(src, [geom], crop=True, filled=False)
        means.append(float(cells.mean()))

wards["mean_elevation_m"] = np.round(means, 1)
print(wards[["NAME_3", "mean_elevation_m"]])
wards.drop(columns="geometry").to_csv(
    "month-03/week-12/my_zonal.csv", index=False
)