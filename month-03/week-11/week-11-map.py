import geopandas as gpd
import matplotlib.pyplot as plt

stream = gpd.read_file("data/processed/stream.gpkg", layer="stream")
boundary = gpd.read_file("processed/Chamwino_wards_boundary_UTM36S.gpkg",layer="Chamwino_wards_boundary_UTM36S",)

fig, ax = plt.subplots(figsize=(7, 8))
boundary.plot(ax=ax, color="#E6F2F3", edgecolor="#037E8E")
stream.plot(ax=ax, color="#355ABF", linewidth=0.8)
ax.set_title("Stream in Chamwino Dodoma")
ax.set_axis_off()

fig.savefig("month-03/week-11/week11_map.png", dpi=150, bbox_inches="tight")
print("Map saved")