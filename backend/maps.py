import googlemaps

from place import *
from time import time
from datetime import datetime
from secret import *
from const import *

SEARCH_MODE = "near" # "near" or "find"
SEARCH_FIELDS = ["name", "place_id", "editorial_summary", "type", "current_opening_hours", "place_id", "price_level", "rating", "review", "formatted_address", "geometry"]

class Maps():
    def __init__(self):
        self.client = googlemaps.Client(key=gmap_token)
        self.language = DEFAULT_LANGUAGE
        self.search_radius = 1000

    def set_location(self, lat: float, lng: float) -> None:
        self.location = (lat, lng)

    def set_search_radius(self, dist: int):
        self.search_radius = dist

    # Generate the string for the location bias
    def __generate_location_bias(self) -> str:
        return "circle:" + str(self.search_radius) + "@" + ",".join(map(str, self.location))

    def search(self, query: str) -> str: 
        results = self.client.find_place(query, "textquery", fields = ['place_id'], location_bias = self.__generate_location_bias(), language = self.language)
        output = list()
        for place in results['candidates']:
            output.append(place['place_id'])
        return output
        
    def find_nearby(self, query: str) -> list: #str
        output = list()
        query_results = self.client.places_nearby(self.location, self.search_radius, query, self.language)
        for r in query_results:
            output.append(r['results']['place_id'])
        return output

    def lookup_id(self, place_id) -> Place:
        response = self.client.place(place_id, fields = SEARCH_FIELDS, language = self.language)["result"]
        place = Place(response["place_id"])
        place.from_raw(response)
        return place

    def gen_route(self, origin: Place, destination: Place) -> Route:
        output = self.client.directions(origin.location, destination.location, mode="driving")
        return Route(origin, destination, output)
    
    def get_dist(self, origin: tuple, destination: tuple = None) -> float:
        if (destination == None):
            destination = self.location
        result = self.client.directions(origin, destination, mode="driving")
        return result['legs'][0]['distance']['value']/1000
    
    def get_time(self, origin: tuple, destination: tuple = None, timezone: str = "EST") -> float:
        if (destination == None):
            destination = self.location
        result = self.client.directions(origin, destination, mode="driving")[0]
        return result['legs'][0]['duration']['text']

    def get_timestamp(self, origin: tuple, destination: tuple = None, timezone: str = "EST") -> float:
        if (destination == None):
            destination = self.location
        result = self.client.directions(origin, destination, mode="driving")[0]
        seconds = result['legs'][0]['duration']['value'] + time()
        return datetime.fromtimestamp(seconds).strftime("%I:%M:%S%p")

#maps = maps()
#maps.set_location([43.90315162960289, -79.43975174603027])
#a = maps.search("Mon Sheong Restaurant")
#print(maps.lookup_id(a['candidates'][0]['place_id'])['result'])