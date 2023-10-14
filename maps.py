import googlemaps
from secret import gmap_token

class maps():
    def __init__(self):
        self.client = googlemaps.Client(key=gmap_token)

    def set_location(self, location: [float, float]) -> None:
        self.location = location

    # Generate the string for the location bias
    def __generate_location_bias(self) -> str:
        return "circle" + self.radius + "@" + ",".join(map(str, self.location))

    def search(self, query: str): #TODO: specify output type
        self.client.find_place(query, "textquery", [], self.__generate_location_bias(), "en")