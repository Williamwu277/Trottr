from flask import Flask, render_template, redirect, request, url_for, make_response, jsonify
import maps as google_maps
import random
import json
from time import time
from datetime import datetime
from place import *
from recommendations import *
from const import *

app = Flask(__name__)

maps = google_maps.Maps()
r = Recommendations()


app.run("localhost", PORT)

@app.route("/home", method=["POST"])
def home():
    points = r.path
    time_stamps, output = [time()], []
    for i in range(1, len(points)):
        time_stamps.append(maps.get_seconds(tuple(points[i]), tuple(points[i+1])) + time_stamps[-1])
    for nxt in time_stamps:
        output.append(datetime.fromtimestamp(nxt).strftime("%I:%M:%S%p"))
    response = []
    for i in range(len(r.path)):
        response.append({
            'name': r.path[i].name,
            'distance': 0,
            'category': "food" if "food" in r.path[i].categories else "entertainment",
            'address': r.path[i].address,
            'location': r.path[i].location,
            'time': output[i]
        })
    return response

@app.route("/init", methods=["POST"])
def init():
    """
    Calls for the server to initialize the Trottr app
    {
        "lat": 43.783079746158016,
        "lng": -79.1872947732961

    }
    """
    maps.set_location(request.args.get("lat"), request.args.get("lng"))
    maps.set_search_radius(5*1000)

    locations = list()

    CATS = ["point of interest", "amusement park", "art gallery", "cafe", "bowling alley", "library", "museum", "park", "restaurant", "shopping mall", "tourist_attraction", "bubble tea", "bakery"]
    temporary = []

    for section in CATS:
        for result in maps.search(section):
            temp = maps.lookup_id(result)
            flag = False
            for next in temporary:
                if next.name == temp.name:
                    flag = True
            if not flag:
                temporary.append(temp)

    random.shuffle(temporary)
    locations = [temporary[next] for next in range(0, min(len(temporary)-1, 15))]

    r.cull_by_price(locations, PRICE_FREE)

    r.import_nearby_stores(locations)


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

    