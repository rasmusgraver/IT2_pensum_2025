import osmnx as ox
import folium as fol


# NB!! 
# NB: MERK at output fra å kjøre denne er at det opprettes en html fil (som du så kan åpne i nettleser)
# NB!! 

sted = "Bergen, Norway"

tags = {"amenity": "cafe"}
kafeer = ox.geometries_from_place(sted, tags=tags)

kafepunkter = kafeer[kafeer.geom_type == "Point"]

m = fol.Map([60.3913, 5.3221], zoom_start=14) # Tegner kartet ved Bergen

for punkt in kafepunkter.geometry:
  fol.CircleMarker([punkt.y, punkt.x]).add_to(m)

m.save("kafeer_Bergen.html")
