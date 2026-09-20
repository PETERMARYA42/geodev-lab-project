## Transport networks, Chamwino-Dodoma
- Extracted 09/09/2026 via Geofabrik
- 32980 features 
- COMPLETENESS: good for my whole study area
- CURRENCY: last update was 2026-09-11. All roads are proper
- POSITIONAL: roads align well with satellite imagery; no systematic offset visible
- ATTRIBUTE: for 'fclass ', which I can use for categorization, all are fine (path, cycleway, footway, residential, service, track, and unclassified), except one row has "unknown"
- FITNESS: good for analysis, as the footpath to truck are well edited

## OSM schools, Chamwino-Dodoma
- Extracted 13/09/2026 via QuickOSM
- 127 features 
- COMPLETENESS: good for my whole study area
- CURRENCY: last update was 2025. All schools are fine
- POSITIONAL: schools align well with satellite imagery; no systematic offset visible
- ATTRIBUTE: all columns corrected and filled according to their data type. 
- FITNESS: good for analysis.

## District boundary, Chamwino-Dodoma
- Extracted 09/09/2026 via Geofabrik
- 1 feature  
- COMPLETENESS: covers my Area of Interest correctly
- CURRENCY: last update was 2026.
- POSITIONAL: it looks similar to Google Satellite in terms of boundary
- ATTRIBUTE: all columns corrected and filled according to their data type. 
- FITNESS: good for use.

## CRS and preparation
- All source layers arrived in EPSG:4326. 
- Study area: Chamwino DC, extracted from Geofabrik wards. 
- All layers were clipped to the study area, then reprojected to EPSG:32736 (UTM 36S)
- Area check: Chamwino DC 9132 km2, matches published figure (Tanzania National Bureau of Statistics (NBS)).
- Working files in D:/GEODAV/WEEK/Processed; raw files untouched
