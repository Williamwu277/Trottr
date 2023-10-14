import googlemaps
from secret import gmap_token

class maps():
    def __init__(self):
        self.client = googlemaps.Client(key=gmap_token)

    def set_location(self, lat: float, lng: float) -> None:
        self.location = (lat, lng)

    # Generate the string for the location bias
    def __generate_location_bias(self) -> str:
        return "circle:" + '1000' + "@" + ",".join(map(str, self.location)) #TODO: make radius customizable and its own attribute

    def search(self, query: str): #TODO: specify output type
        self.client.find_place(query, "textquery", [], self.__generate_location_bias(), "en")