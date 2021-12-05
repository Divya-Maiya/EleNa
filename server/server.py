# Handle front end requests
# Instantiate controller

from flask import Flask, request, render_template
import json
import webbrowser

from controller.controller import Controller
from model.model import Model
from utils import map_utils
from utils.map_utils import get_node_from_address

app = Flask(__name__)
# graphs = {}
graph = map_utils.load_graph()
webbrowser.open('http://localhost:5000', new=2)


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", token="Hello SEleNa")


@app.route('/route', methods=['POST'])
def route():

    data = json.loads(request.data)
    print(data)

    goal = data['goal']
    algo = data['algorithm']

    # Get Lat Long of Address from Nominatim Geocoding API
    try:
        start_node = get_node_from_address(graph, data['start'])
        dest_node = get_node_from_address(graph, data['dest'])
    except Exception as e:
        print(e)
        return {'error': str(e)}, 501

    limit = float(data['limit']) / 100

    model = Model()
    model.set_mode(goal)
    model.set_limit(limit)
    model.set_algorithm(algo)
    model.set_source(start_node)
    model.set_destination(dest_node)

    ctr = Controller()
    ctr.set_model(model)

    return ctr.handle_request(graph)
