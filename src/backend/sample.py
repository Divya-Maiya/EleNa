# from src.backend.controller.controller import Controller
# from src.backend.model.model import Model
# from src.backend.utils.map_utils import *
#
# # apiKey = "AIzaSyBQIIBs6JaQjM3OViYfk_KpuKdnUGZTq-o"
# #
# # file_name = "data/graph_Amherst.pkl"
# # get_map("Amherst", "Massachusetts", "USA", apiKey, file_name)
#
# graph = load_map("data/graph_Amherst.pkl", changeDir=0)
# # ox.plot_graph(graph)
# # print(g)
#
# model = Model()
# controller = Controller()
# controller.set_model(model)
# # model.set_mode("plain")
# model.set_limit(0.5)
# model.set_destination("1 Rolling Green Dr, Amherst, MA 01002")
# model.set_source("Brandywine Dr, Amherst, MA 01002")
# # model.set_source("251-255 Geneva Avenue, Boston, MA 02121, United States of America")
# # model.set_destination("15 Penfield Street, Boston, MA 02131, United States of America")
# model.set_algorithm("Dijkstra")
#
# # print(get_coordinates("51A Humboldt Avenue, Roxbury, MA 02119 Roxbury Boston Massachusetts United States"))
# # print(get_coordinates("Bragdon Street, Boston, MA 02130-0947, United States"))
# # controller.handle_request(graph)
#
# model.set_mode("max")
# controller.handle_request(graph, plot_local=1)
#
# # model.set_mode("min")
# # controller.handle_request(graph)
#
#
# # lat, lng = 42.3676084, -71.0218168
# # node, dist = ox.nearest_nodes(graph, float(lat), float(lng), return_dist=True)
# # print(dist)