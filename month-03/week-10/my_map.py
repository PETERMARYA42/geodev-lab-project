import geopandas as gpd
import matplotlib.pyplot as plt

my_roads = gpd.read_file("Processed/roads_UTM36S.gpkg", layer="roads_UTM36S")

fig, ax = plt.subplots(figsize=(7, 8))
my_roads.plot(ax=ax, color="#E6121D", edgecolor="#037E8E")
ax.set_title("Roads in Chamwino District")
ax.set_axis_off()

fig.savefig("month-03/week-10/roads_map.png", dpi=150, bbox_inches="tight")
print("Map saved")