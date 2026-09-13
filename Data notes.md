# Data notes

## District boundary - Geofabrik 
- Source: https://download.geofabrik.de/africa/tanzania-latest-internal-free.shp.zip
- Downloaded: 09/09/2026
- 603 features, polygons
- Columns: osm_id(integer), code(integer), fclass(text), name(text)
- No nulls in district_name
- Covers my Area of Interest fully

## Transport networks - Geofabrik 
- Source: https://download.geofabrik.de/africa/tanzania-latest-internal-free.shp.zip
- Downloaded: 09/09/2026
- Columns: fid(integer), osm_id(integer), code(integer), fclass(text), name(text), ref, oneway(text), maxspeed(integer), layer(integer), bridge(text), tunnel(text)
- 32980 features, lines
- Only 315 features have names; the rest are null
- Coverage is reasonable

## OSM schools, extracted via QuickOSM
- Query: amenity=* within chamwino_dc extent 
- Extracted: 13/09/2026
- 127 features, points
- No nulls in the name column, and they are nicely distributed

## Waterways - Geofabrik 
- Source: https://download.geofabrik.de/africa/tanzania-latest-internal-free.shp.zip
- Downloaded: 09/09/2026
- Columns: fid(integer), osm_id(integer), code(integer), fclass(text), width(integer), name(text)
- 440 features, lines
- Only 25 features out of 440 have names  
- In the fclass column, categorized as stream and river

## Population - WorldPop 
- Source: https://www.worldpop.org 




