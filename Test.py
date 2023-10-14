import cohere
import random
from place import Place

# remove API key when pushing to github
api_key = ""
co = cohere.Client(api_key)

'''
Variables
- min price
- max price
- location
- distances / bus routes etc
- rating
- time open
- name
- type (food etc)
'''

# stores dictionary of each place by name
locations = []

# create random plans
def create_plans():

    _prompt = """Given a list of locations and their type, design twenty itineraries of one to five items. Two (foods) cannot be put together.
    \nPlaces: Pool (entertainment), Library (entertainment), Harveys (food), Tim Hortons (food)
    Itinerary:\n1. Tim Hortons, Library, Harveys\n2. Harveys, Pool, Tim Hortons\n--
    Places: Mc Donalds (food), Chuckee Cheese (entertainment), Disco (entertainment), Egg Smart (food)
    Itinerary:\n1. Mc Donalds, Chuckee Cheese, Egg Smart\n2.  Chuckee Cheese, Egg Smart, Disco\n--\nPlaces:"""
    
    for location in locations:
        if "food" in location.type:
            _prompt += " " + location.name + " (food)\n"
        else:
            _prompt += " " + location.name + " (" + location.type[random.randint(0, len(location.type)-1)] + ")\n"
    _prompt += "Itinerary:\n"

    response = co.generate(
        model='command',
        prompt=_prompt,
        max_tokens=500,
        temperature=1,
        k=0,
        stop_sequences=['--'],
        return_likelihoods='NONE')
    print('Prediction: {}'.format(response.generations[0].text))
