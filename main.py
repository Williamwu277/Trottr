import maps as google_maps
from place import *
from recommendations import Recommendations

if __name__ == "__main__":
    maps = google_maps.Maps()
    maps.set_location(43.90269544941747, -79.43994488708786)
    maps.set_distance(5*1000)
    #ai = reccomendations.Reccomendations()

    locations = list()
    routes = list()

    for result in maps.search("bubble tea")["results"]:
        temp = maps.lookup_id(result["place_id"])
        locations.append(temp)
    
    r = Recommendations()

    r.cull_by_price(locations, 0, 0)
    print(locations)
    #r.import_nearby_stores(locations)



