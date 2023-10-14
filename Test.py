from secret import*
import cohere
import random
from place import Place

# remove API key when pushing to github
co = cohere.Client(cohere_token)

# stores dictionary of each place by name
locations = []

# query for approximate amount of time visitors spend in each place
def import_nearby_stores(places):

    _prompt = open("prompts/timeGenerationPrompt.txt", 'r').readlines()
    _prompt += "Places:\n"

    for place in places:
        _prompt += place.name + ": " + place.description + "\n"

    _prompt += "Results:\n"

    response = co.generate(
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

        locations[place] = time

# generate a place that matches a certain theme and time limit
def add_place(places, theme, time_requirement):

    _prompt = open("prompts/locationGenerationPrompt.txt", 'r').readlines()
    _prompt += "Places:\n"

    for place in places:
        _prompt += place.name + ": " + place.description + "\n"
    
    _prompt += "Theme: " + theme + "\nTime needed:" + time_requirement + "\nResults:\n"

    response = co.generate(
        model = 'command',
        prompt = _prompt,
        max_tokens = 100,
        temperature = 1,
        k = 0,
        stop_sequences = ['--'],
        return_likelihoods = "NONE"
    ).generations[0].text

    return response.rstrip()
