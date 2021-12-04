from utils.graph_utils import weight_function, get_path_length, get_path_elevation
import heapq
from itertools import count
import networkx as nx


def dijkstra(graph, start_node, dest_node, limit, mode):
    if mode == "max":
        return maximum_elevation(graph, start_node, dest_node, limit)
    else:
        return minimum_elevation(graph, start_node, dest_node, limit)


def get_shortest_path(graph, start_node, dest_node, edge_weight='length'):
    weight = weight_function(graph, edge_weight)
    paths = {start_node: [start_node]}
    successor_graph = graph._succ if graph.is_directed() else graph._adj

    push = heapq.heappush
    pop = heapq.heappop
    dist = {}  # Dictionary of Final distances
    seen = {}
    c = count()
    queue = []

    if start_node not in graph:
        return []  # Figure out way to handle exceptions properly

    seen[start_node] = 0
    push(queue, (0, next(c), start_node))
    while queue:
        d, _, v = pop(queue)
        if v in dist:
            continue  # already searched this node
        dist[v] = d
        if v == dest_node:
            break
        for u, e in successor_graph[v].items():
            cost = weight(v, u, e) + 1
            if cost is None:
                continue

            vu_dist = dist[v] + cost
            if u in dist:
                if vu_dist < dist[u]:
                    pass  # Contradictory paths found, negative weights?
            elif u not in seen or vu_dist < seen[u]:
                seen[u] = vu_dist
                push(queue, (vu_dist, next(c), u))
                paths[u] = paths[v] + [u]

    return paths[dest_node]


def maximum_elevation(graph, start_node, dest_node, limit):
    """Gets the shortest path within a path length limit, optimizing for maximum elevation.
    Parameters
    ----------
    start_node : node
        starting point node for the path
    dest_node : node
        destination node for the path
    Returns
    ------
    list of nodes that form the discovered path
    """

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


def minimum_elevation(graph, start_node, dest_node, limit):

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
