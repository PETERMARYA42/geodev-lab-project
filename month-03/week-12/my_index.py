import numpy as np
import rasterio

folder = "my_landsat/"
scene = "LC09_L2SP_168064_20260924_20260925_02_T1"

with rasterio.open(folder + scene + "_SR_B3.TIF") as src:
    green_raw = src.read(1).astype("float32")
    profile = src.profile
    
with rasterio.open(folder + scene + "_SR_B5.TIF") as src:
    nir_raw = src.read(1).astype("float32")
    
valid = (green_raw > 0) & (nir_raw > 0)

green = green_raw + 0.0000275 - 0.2
nir = nir_raw + 0.0000275 - 0.2

ndwi = np.full(green.shape, -9999, dtype="float32")
total = nir + green
ok = valid & (total != 0)
ndwi[ok] = (nir[ok] - green[ok]) / total[ok]
low = round(float(ndwi[ok].min()), 3)
high = round(float(ndwi[ok].max()), 3)
print("NDWI range:", low, "to", high)
print("Mean NDWI:", round(float(ndwi[ok].mean()), 3))

profile.update(dtype="float32", nodata=-9999, count=1)
with rasterio.open("data/processed/ndwi.tif", "w", **profile) as dst:
    dst.write(ndwi, 1)
print("Saved data/processed/ndwi.tif")