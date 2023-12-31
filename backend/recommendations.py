import cohere as cohere_api
from secret import *
from place import Place, strip_nonalphanumerical

PRICE_FREE = (0, 0)
PRICE_CHEAP = (0, 1)
PRICE_NORM = (1, 3)
PRICE_EXP = (2, 4)
PRICE_LUX = (3, 4)
PRICE_FULL = (0, 4)

CATEGORIES = {
    'snacks':['bubble tea', 'cafe', 'bakery'],
    'meals':["restaurant"],
    'outdoor':["point of interest", "tourist_attraction", "park", "amusement park"],
    'indoor':["arcade", "art gallery", "bowling alley", "museum", "library", "shopping mall"]
}

class Recommendations:
    def __init__(self):
        self.cohere = cohere_api.Client(cohere_token)
        # stores dictionary of each place by name
        self.locations = {}
        self.path = []
        self.themequeue = ""
        self.themequeue_options = []
        self.themelocs = []

    # query for approximate amount of time visitors spend in each place
    def import_nearby_stores(self, places):

        _prompt = open("prompts/timeGenerationPrompt.txt", 'r').read()
        _prompt += "Places:\n"

        for place in places:
            _prompt += place.name + ": " + place.desc + "\n"

        _prompt += "Results:\n"
        print(_prompt)

        response = self.cohere.generate(
            model = 'command',
            prompt = _prompt,
            max_tokens = 50000,
            temperature = 1,
            k = 0,
            stop_sequences = ['--'],
            return_likelihoods = 'NONE'
        )
        print(response.generations[0].text)
        response = response.generations[0].text.split("\n")
        index = 0
        for line in response:
            l = line.split(": ")
            time = l[1].split(' ')[0]

            self.locations[strip_nonalphanumerical(places[index].name)] = time
            index += 1

    # generate a place that matches a certain theme and time limit
    def add_place(self, places, nexttheme:str=None, time_requirement=60):
        print(self.locations)
        print(places)
        if (nexttheme == None):
            nexttheme = "entertainment"
        theme = self.themequeue
        self.themequeue = nexttheme
        _prompt = open("prompts/locationGenerationPrompt.txt", 'r').read()
        _prompt += "Places:\n"
        print(self.locations)
        for place in places:
            _prompt += place.name + ": " + place.desc + " (" + str(self.locations[strip_nonalphanumerical(place.name)]) + " minutes) (" + str(place.rating) + " stars)\n"
   
        _prompt += "Theme: " + theme + "\nTime needed:" + str(time_requirement) + " minutes\nResults:\n"

        response = self.cohere.generate(
            model = 'command',
            prompt = _prompt,
            max_tokens = 50000,
            temperature = 1,
            k = 0,
            stop_sequences = ['--'],
            return_likelihoods = "NONE"
        ).generations[0].text

        print(response)

        place = None
        for nxt in places:
            print(nxt.name)
            if nxt.name in response:
                place = nxt
                break
        if (place != None):
            self.path.append(place)

    def cull_by_price(self, locations: list, price_range: tuple):
        for i in range(len(locations)-1, -1, -1):
            if not (price_range[0] <= locations[i].price_rating and locations[i].price_rating <= price_range[1]): 
                locations.pop(i)