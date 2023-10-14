import googlemaps

from place import Place

from secret import *
from const import *

SEARCH_MODE = "near" # "near" or "find"

class Maps():
    def __init__(self):
        self.client = googlemaps.Client(key=gmap_token)
        self.language = default_language

    def set_location(self, lat: float, lng: float) -> None:
        self.location = (lat, lng)

    # Generate the string for the location bias
    def __generate_location_bias(self) -> str:
        return "circle:" + '1000' + "@" + ",".join(map(str, self.location)) #TODO: implement self.radius

    def search(self, query: str): #TODO: specify output type
        if SEARCH_MODE == "find":
            return self.client.find_place(query, "textquery", fields = [], location_bias = self.__generate_location_bias(), language = self.language)
        elif SEARCH_MODE == "near":
            return self.client.places_nearby(self.location, '1000', query, self.language)

    def lookup_id(self, id) -> Place:
        response = self.client.place(id, fields = "", language = self.language)
        place = Place()
        place.from_raw(response)
        return place

#maps = maps()
#maps.set_location([43.90315162960289, -79.43975174603027])
#a = maps.search("Mon Sheong Restaurant")
#print(maps.lookup_id(a['candidates'][0]['place_id'])['result'])