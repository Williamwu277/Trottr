import cohere as cohere_api
from secret import *
from place import Place



class Recommendations:
    def __init__(self):
        self.cohere = cohere_api.Client(api_key)
        # stores dictionary of each place by name
        self.locations = []

    # query for approximate amount of time visitors spend in each place
    def import_nearby_stores(self, places):

        _prompt = open("prompts/timeGenerationPrompt.txt", 'r').readlines()
        _prompt += "Places:\n"

        for place in places:
            _prompt += place.name + ": " + place.description + "\n"

        _prompt += "Results:\n"

        response = self.cohere.generate(
            model = 'command',
            prompt = _prompt,
            max_tokens = 1000,
            temperature = 1,
            k = 0,
            stop_sequences = ['--'],
            return_likelihoods = 'NONE'
        ).generations[0].text.split("\n")
        response.pop(-1)

        for line in response:
            l = line.split(": ")
            place = line[0]
            time = line[1].split(' ')[0]

            self.locations[place] = time

    # generate a place that matches a certain theme and time limit
    def add_place(self, places, theme, time_requirement):

        _prompt = open("prompts/locationGenerationPrompt.txt", 'r').readlines()
        _prompt += "Places:\n"

        for place in places:
            _prompt += place.name + ": " + place.description + "\n"
        
        _prompt += "Theme: " + theme + "\nTime needed:" + time_requirement + "\nResults:\n"

        response = self.cohere.generate(
            model = 'command',
            prompt = _prompt,
            max_tokens = 100,
            temperature = 1,
            k = 0,
            stop_sequences = ['--'],
            return_likelihoods = "NONE"
        ).generations[0].text

        return response.rstrip()
