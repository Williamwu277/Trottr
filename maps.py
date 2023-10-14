import googlemaps

from place import Place

from secret import *
from const import *

SEARCH_MODE = "near" # "near" or "find"
SEARCH_FIELDS = ["name", "place_id", "editorial_summary", "type", "current_opening_hours", "place_id", "price_level", "rating", "review", "formatted_address"]

class Maps():
    def __init__(self):
        self.client = googlemaps.Client(key=gmap_token)
        self.language = default_language
        self.dist = 1000

    def set_location(self, lat: float, lng: float) -> None:
        self.location = (lat, lng)

    def set_distance(self, dist: int):
        self.dist = dist

    # Generate the string for the location bias
    def __generate_location_bias(self) -> str:
        return "circle:" + str(self.dist) + "@" + ",".join(map(str, self.location)) #TODO: implement self.radius

    def search(self, query: str): #TODO: specify output type
        if SEARCH_MODE == "find":
            return self.client.find_place(query, "textquery", fields = [], location_bias = self.__generate_location_bias(), language = self.language)
        elif SEARCH_MODE == "near":
            return self.client.places_nearby(self.location, self.dist, query, self.language)

    def lookup_id(self, place_id) -> Place:
        response = self.client.place(place_id, fields = SEARCH_FIELDS, language = self.language)["result"]
        place = Place(response["place_id"])
        place.from_raw(response)
        return place

    def gen_route(self, origin: tuple, destination: tuple):
        return self.client.directions(origin, destination, mode="driving")


#maps = maps()
#maps.set_location([43.90315162960289, -79.43975174603027])
#a = maps.search("Mon Sheong Restaurant")
#print(maps.lookup_id(a['candidates'][0]['place_id'])['result'])