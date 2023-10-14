import googlemaps
from secret import gmap_token

class maps():
    def __init__(self):
        self.client = googlemaps.Client(key=gmap_token)

    def set_location(self, lat: float, lng: float) -> None:
        self.location = (lat, lng)

    # Generate the string for the location bias
    def __generate_location_bias(self) -> str:
        return "circle:" + self.radius + "@" + ",".join(map(str, self.location))

    def search(self, query: str): #TODO: specify output type
        return self.client.find_place(query, "textquery", [], self.__generate_location_bias(), "en")

    def search_by_id(self, id) :
        return self.client.place(id)

#maps = maps()
#maps.set_location([43.90315162960289, -79.43975174603027])
#a = maps.search("Mon Sheong Restaurant")
#print(maps.search_by_id(a['candidates'][0]['place_id'])['result'])