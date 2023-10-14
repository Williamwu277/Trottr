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

    count = 0
    for result in maps.search("point of interest")["results"]:
        temp = maps.lookup_id(result["place_id"])
        locations.append(temp)
        if count > 9:
            break
    
    r = Recommendations()

    r.cull_by_price(locations, 0, 0)
    print(locations)
    r.import_nearby_stores(locations)
    print(r.add_place(locations, "park", 60))



