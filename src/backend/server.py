# Handle front end requests
# Instantiate controller

from flask import Flask, request, render_template
import json
import webbrowser

from src.backend.controller.controller import Controller
from src.backend.model.model import Model
from utils import map_utils

app = Flask(__name__)
# graphs = {}
# print(os.getcwd())

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
    city = data['city']

    map_file = "data/graph_" + city + ".pkl"
    graph = map_utils.load_map(map_file)

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
