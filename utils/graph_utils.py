def shortest_path_optimizer(graph, weight='length'):
    if weight == 'length':
        def weight_(source, dest, edge_data):
            return min(attr.get(weight, 1) for attr in edge_data.values())

    elif weight == 'grade':
        def weight_(source, dest, edge_data):
            try:
                return max(0, edge_data['grade'])
            except:
                return 0
    elif weight == 'elevation_change':
        def weight_(source, dest, edge_data):
            try:
                elevation_diff = graph.nodes[dest]['elevation'] - graph.nodes[source]['elevation']
                return max(elevation_diff, 0)
            except:
                print("elevation not found: ", source, dest)
                return 0
    return weight_


def get_path_length(graph, path):
    length = 0
    for i in range(len(path) - 1):
        length += graph[path[i]][path[i + 1]][0]['length']
    return length


def get_path_elevation(graph, path):
    elevation = 0
    for i in range(len(path) - 1):
        elevation += max(0, graph.nodes[path[i + 1]]['elevation'] - graph.nodes[path[i]]['elevation'])
    return elevation


def maximum_elevation(graph, start_node, dest_node, limit, get_shortest_path):
    shortest_path = get_shortest_path(graph, start_node, dest_node, edge_weight="length")
    shortest_path_length = get_path_length(graph, shortest_path)
    max_path_length = shortest_path_length * (1 + limit)
    max_path = []
    length_allowance = max_path_length - shortest_path_length
    if length_allowance < 15:
        return shortest_path

    # Iterate through each pair of nodes and find a subpath that can maximize elevation within a path
    # length constraint
    for i in range(0, len(shortest_path) - 1):
        cur_node = shortest_path[i]
        next_node = shortest_path[i + 1]
        min_distance = graph[cur_node][next_node][0]['length']
        allowance = length_allowance * (min_distance / shortest_path_length)
        highest_elevation = -1
        best_path = []

        # find all paths from cur_node to next_node and get the path length and elevation, add to original path
        for path in nx.all_simple_paths(graph, cur_node, next_node, cutoff=5):
            path_elevation = get_path_elevation(graph, path)
            path_length = get_path_length(graph, path)

            if path_elevation > highest_elevation:
                if path_length <= allowance + min_distance:
                    highest_elevation = path_elevation
                    best_path = path

        best_path_length = get_path_length(graph, best_path)
        length_allowance -= (best_path_length - min_distance)

        for j in best_path[:-1]:
            max_path.append(j)

    max_path.append(dest_node)
    return max_path


def minimum_elevation(graph, start_node, dest_node, limit, get_shortest_path):
    shortest_path = get_shortest_path(graph, start_node, dest_node, edge_weight="length")
    shortest_path_length = get_path_length(graph, shortest_path)
    max_path_length = shortest_path_length * (1 + limit)

    if limit < 0.05:
        return shortest_path
    # calculate the smallest elevation path using elevation/grade
    least_elevation = get_shortest_path(graph, start_node, dest_node, edge_weight="elevation_change")
    least_elevation_length = get_path_length(graph, least_elevation)

    # if the path with smallest elevation is longer than the maximum allowed path, go through each node
    # and find the shortest path from the end to the beginning, thereby optimizing for elevation and path length
    if least_elevation_length > max_path_length:
        length = len(least_elevation)
        for i in range(2, length + 1):
            node = least_elevation[-i]
            path_length_to_node = get_path_length(graph, least_elevation[:-i + 1])
            node_to_dest_node_shortest = shortest_path(node, dest_node)
            new_path_length = get_path_length(graph, node_to_dest_node_shortest)
            if path_length_to_node + new_path_length <= max_path_length:
                return least_elevation[:-i] + node_to_dest_node_shortest
    else:
        return least_elevation


def get_l1_distance(graph, start, goal):
    """Calculates the L1 distance between two nodes.
    Parameters
    ----------
    :param graph: graph object
    :param goal: destination node for the path
    :param start: starting point node for the path
    """

    amherst_graph = graph
    start_x, start_y = amherst_graph.nodes[start]['x'], amherst_graph.nodes[start]['y']
    end_x, end_y = amherst_graph.nodes[goal]['x'], amherst_graph.nodes[goal]['y']
    # return 0 # Dijkstra, essentially
    return ((end_x - start_x) ** 2 + (end_y - start_y) ** 2) ** 0.5
