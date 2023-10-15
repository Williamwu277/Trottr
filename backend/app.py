from flask import Flask, render_template, redirect, request, url_for, make_response, jsonify
import maps as google_maps
import random
from place import *
from recommendations import *
from const import *

app = Flask(__name__)

maps = google_maps.Maps()
r = Recommendations()

maps.set_location(43.90269544941747, -79.43994488708786)
maps.set_search_radius(5*1000)

locations = list()
routes = list()

CATS = ["point of interest", "amusement park", "art gallery", "cafe", "bowling alley", "library", "museum", "park", "restaurant", "shopping mall", "tourist_attraction", "bubble tea", "bakery"]
temporary = []

for section in CATS:
    for result in maps.search(section):
        temp = maps.lookup_id(result)
        if not temp in locations:
            temporary.append(temp)

random.shuffle(temporary)
locations = [temporary[next] for next in range(0, min(len(temporary)-1, 15))]

r.cull_by_price(locations, PRICE_FREE)
print(locations)

r.import_nearby_stores(locations)

print(r.add_place(locations, "park", 60))


app.run("localhost", PORT)


@app.route("/search", methods=["POST"])
def search():
    """
    Search for a location given text information about it
    {
        "query": "University of Toronto Scarborough Campus"
        "lat": "43.783079746158016",
        "long": "-79.1872947732961"
    }
    """
    places = maps.search(request.args.get("query"))
    response = []
    for place_id in places:
        place = maps.lookup_id(place_id)
        response.append({
            'name': place.name,
            'distance': maps.get_dist((float(request.args.get("lat")), float(request.args.get("long")))),
            'category': "food" if "food" in place.categories else "entertainment",
            'address': place.address,
            'location': place.location,
            'time': maps.get_time((float(request.args.get("lat")), float(request.args.get("long"))))
        })
    return response

@app.route("/suggested", methods=["POST"])
def suggested():
    """
    Find places near user's set location
    {
        "query": "Restaurants"
    }
    """
    return maps.find_nearby(request.arg.get("query")) #TODO: parse place info