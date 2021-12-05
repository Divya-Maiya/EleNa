from utils.graph_utils import shortest_path_optimizer, get_path_length, get_path_elevation, maximum_elevation, \
    minimum_elevation
import heapq
from itertools import count


def get_shortest_path(graph, start_node, dest_node, edge_weight='length'):
    weight = shortest_path_optimizer(graph, edge_weight)
    paths = {start_node: [start_node]}
    successor_graph = graph._succ if graph.is_directed() else graph._adj

    push = heapq.heappush
    pop = heapq.heappop
    dist = {}  # Dictionary of Final distances
    seen = {}
    c = count()
    queue = []

    if start_node not in graph:
        print("Start node is not in the map. Please restart with the correct start node")
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


def dijkstra(graph, start_node, dest_node, limit, mode):
    if mode == "max":
        return maximum_elevation(graph, start_node, dest_node, limit, get_shortest_path)
    else:
        return minimum_elevation(graph, start_node, dest_node, limit, get_shortest_path)
