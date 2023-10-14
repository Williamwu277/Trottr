import maps as google_maps
from place import *
import reccomendations

if __name__ == "__main__":
    maps = google_maps.Maps()
    maps.set_location(43.90269544941747, -79.43994488708786)
    maps.set_distance(10*1000)
    #ai = reccomendations.Reccomendations()

    locations = list()
    routes = list()

    for result in maps.search("bubble tea")["results"]:
        temp = maps.lookup_id(result["place_id"])
        locations.append(temp)



