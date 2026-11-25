import matplotlib.pyplot as plt
import rasterio

with rasterio.open("data/processed/ndwi.tif") as src:
    ndwi = src.read(1, masked=True)
fig, ax = plt.subplots(figsize=(7,8))
image = ax.imshow(ndwi, cmap="RdYlBu", vmin= 0.2, vmax= 0.9)
fig.colorbar(image, ax= ax, label="NDWI")
ax.set_title("Water index, Chamwino")
ax.set_axis_off()
fig.savefig("month-03/week-12/my_map.png", dpi=150, bbox_inches="tight")
print("Saved my_map.png")