# Handle front end requests
# Instantiate controller
import os

from flask import Flask, request, render_template
import json
import webbrowser

from controller.controller import Controller
from model.model import Model
from utils import map_utils

app = Flask(__name__)
# graphs = {}
print(os.getcwd())
graph = map_utils.load_map()

webbrowser.open('http://localhost:5000', new=2)


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", token="Hello SEleNa")


@app.route('/route', methods=['POST'])
def route():
    data = json.loads(request.data)
    print(data)

    mode = data['mode']
    algo = data['algorithm']

    # Get Lat Long of Address from Nominatim Geocoding API
    # try:
    #     start_node = get_node_from_address(graph, data['start'])
    #     dest_node = get_node_from_address(graph, data['dest'])
    # except Exception as e:
    #     print(e)
    #     return {'error': str(e)}, 501

    limit = float(data['limit']) / 100

    model = Model()
    model.set_mode(mode)
    model.set_limit(limit)
    model.set_algorithm(algo)
    model.set_source(data['start'])
    model.set_destination(data['dest'])

    ctr = Controller()
    ctr.set_model(model)

    return ctr.handle_request(graph)


if __name__ == "__main__":
    app.run()
