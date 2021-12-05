from controller.controller import Controller
from model.model import Model
from utils.map_utils import get_map, get_coordinates
from utils.map_utils import load_map
import osmnx as ox

# apiKey = "AIzaSyBQIIBs6JaQjM3OViYfk_KpuKdnUGZTq-o"
#
# get_map("Boston", "Massachusetts", "USA", apiKey)

graph = load_map()
# ox.plot_graph(graph)
# print(g)

model = Model()
controller = Controller()
controller.set_model(model)
model.set_mode("plain")
model.set_limit(0.5)
# model.set_source("140 Commonwealth Avenue, Chestnut Hill, MA 02467")
model.set_source("251-255 Geneva Avenue, Boston, MA 02121, United States of America")
model.set_destination("15 Penfield Street, Boston, MA 02131, United States of America")
model.set_algorithm("Dijkstra")

# print(get_coordinates("51A Humboldt Avenue, Roxbury, MA 02119 Roxbury Boston Massachusetts United States"))
# print(get_coordinates("Bragdon Street, Boston, MA 02130-0947, United States"))
controller.handle_request(graph)


# lat, lng = 42.3676084, -71.0218168
# node, dist = ox.nearest_nodes(graph, float(lat), float(lng), return_dist=True)
# print(dist)