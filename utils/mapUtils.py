import osmnx as ox
import pickle as pkl


def get_coordinates(graph, address):
    return ox.geocode(address)


def get_map(city, state, country, apiKey):
    graph = None
    # save pkl file


def load_map():
    with open("data/boston.pkl", 'rb') as infile:
        graph = pkl.load(infile)
        return graph


def get_node_from_address(graph, address):
    try:
        latlng = get_coordinates(graph, address)
        node, dist = ox.get_nearest_node(graph, latlng, return_dist=True)
        if dist > 10000:
            raise Exception("{} is not currently included in Routing Capabilities".format(address))
        return node
    except:
        raise Exception("Could not find location '{}'".format(address))


# Refactor
def convert_path(graph, path):
    final_path = []
    lengths_and_elevations = []

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
    last_node = graph.nodes[next_node]
    final_path.append((last_node['x'], last_node['y']))
    lengths_and_elevations.append({'length': 0, 'elevation': last_node['elevation']})
    return final_path, lengths_and_elevations