from flask import Flask, render_template, redirect, request, url_for, make_response, jsonify
import maps as google_maps
from place import *
from recommendations import *
from const import *

app = Flask(__name__)

maps = google_maps.Maps()
r = Recommendations()

maps.set_location()

maps.set_location(43.90269544941747, -79.43994488708786)
maps.set_distance(5*1000)

locations = list()
routes = list()

count = 0
for result in maps.search("point of interest")["results"]:
    temp = maps.lookup_id(result["place_id"])
    locations.append(temp)
    if count > 9:
        break

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
    }
    """
    return maps.search(request.args.get("query")) #TODO: parse place info

@app.route("/suggested", methods=["POST"])
def suggested():
    """
    Find places near user's set location
    {
        "query": "Restaurants"
    }
    """
    return maps.find_nearby(request.arg.get("query")) #TODO: parse place info