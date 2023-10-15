import maps as google_maps
from place import *
from recommendations import *

if __name__ == "__main__":
    maps = google_maps.Maps()
    #maps.set_location(43.90269544941747, -79.43994488708786)
    maps.set_location(43.902741831347065, -79.43988051407273)
    maps.set_search_radius(5*1000)
    #ai = reccomendations.Reccomendations()

    locations = list()
    routes = list()

    count = 0
    for result_id in maps.search("bubble tea"):
        temp = maps.lookup_id(result_id)
        locations.append(temp)
        if count > 9:
            break
    
    r = Recommendations()

    r.cull_by_price(locations, PRICE_FULL)
    print(locations)

    #//r.import_nearby_stores(locations)

    #print(r.add_place(locations, "bubble tea", 60))


    places = maps.search("mcdonalds")
    response = []
    for place_id in places:
        place = maps.lookup_id(place_id)
        response.append({
            'name': place.name,
            #'distance': maps.get_dist((float(request.args.get("lat")), float(request.args.get("long")))),
            'category': "n/a",
            'address': place.address,
            'location': place.location,
            'time': maps.get_time((43.896227010937835, -79.44231796965393))
        })
    print(response)


