import os

import osmnx as ox
import pickle as pkl

"""
Map related utils for oxmnx library
"""


def get_coordinates(address):
    return ox.geocode(address)


"""
get_map(): Saves the map of a particular city
Inputs: 
  - city: City for the map
  - state: State
  - country: Country 
  - api_key: Google API Key
Output: 
    None
"""


def get_map(city, state, country, api_key, file_name):
    print(os.getcwd())
    os.chdir("backend")
    # downloading local map
    query = {'city': city, 'state': state, 'country': country}
    # query = {'state': state, 'country': country}
    graph_orig = ox.graph_from_place(query, network_type='drive')

    # adding elevation data from GoogleMaps
    graph_orig = ox.add_node_elevations_google(graph_orig, api_key=api_key)
    graph_orig = ox.add_edge_grades(graph_orig)
    pkl.dump(graph_orig, open(file_name, "wb"))

    # projecting map on to 2D space
    # graph_projection = ox.project_graph(graph_orig)
    # pkl.dump(graph_projection, open("data/graph_projected.pkl", "wb"))


"""
load_map(): Loads the map of a particular city saved by get_map()
Inputs: 
  None
Output: 
  graph object
"""


def load_map(filepath, changeDir=0):
    print(os.getcwd())
    # if changeDir == 1:
    #     os.chdir("src/backend")

    with open(filepath, 'rb') as infile:
        graph_orig = pkl.load(infile)
        # graph_orig = ox.add_node_elevations_google(graph_orig, api_key="AIzaSyBQIIBs6JaQjM3OViYfk_KpuKdnUGZTq-o")
        # graph_orig = ox.add_edge_grades(graph_orig)
        return graph_orig


def get_node_from_address(graph, address):
    try:
        lat, lng = get_coordinates(address)
        node, dist = ox.nearest_nodes(graph, lng, lat, return_dist=True)
        if dist / 10000 > 10000:
            raise Exception("{} is not currently included in Routing Capabilities".format(address))
        return node
    except:
        raise Exception("Could not find location '{}'".format(address))


# TODO Refactor
def convert_path(graph, path):
    final_path = []
    lengths_and_elevations = []

    next_node = None
    for i in range(len(path) - 1):
        node_id = path[i]
        next_node = path[i + 1]
        x = graph.nodes[node_id]['x']
        y = graph.nodes[node_id]['y']
        elevation = graph.nodes[node_id]['elevation']
        edge = graph[node_id][next_node][0]
        length = 0

        if 'length' in edge:
            length = edge['length']
        grade = 0
        if 'grade' in edge:
            grade = max(0, edge['grade'])
        final_path.append((x, y))
        lengths_and_elevations.append({'length': length, 'elevation': elevation, 'grade': grade})

    # Add Last Node
    if next_node is None:
        raise Exception("Unable to find a route")

    last_node = graph.nodes[next_node]
    final_path.append((last_node['x'], last_node['y']))
    lengths_and_elevations.append({'length': 0, 'elevation': last_node['elevation']})
    return final_path, lengths_and_elevations
