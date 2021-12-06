from abc import ABC

from src.backend.algorithm.algorithm import *
from src.backend.utils.graph_utils import *
import heapq
from itertools import count

"""
To get the shortest path using Dijkstra's algorithm
"""


class Dijkstra(Algorithm):
    def get_shortest_path(self, graph, start_node, dest_node, edge_weight='length'):
        optimizer_func = shortest_path_optimizer(graph, edge_weight)
        paths = {start_node: [start_node]}
        new_graph = graph._succ if graph.is_directed() else graph._adj

        push = heapq.heappush
        pop = heapq.heappop
        # Dictionary for final distances
        distances = {}
        visited = {}
        c = count()
        queue = []

        if start_node not in graph:
            raise Exception("Start node is not in the map. Please restart with the correct start node")

        visited[start_node] = 0
        push(queue, (0, next(c), start_node))
        while queue:
            d, _, v = pop(queue)
            if v in distances:
                continue  # already searched this node
            distances[v] = d
            if v == dest_node:
                break
            for u, e in new_graph[v].items():
                cost = optimizer_func(v, u, e) + 1
                if cost is None:
                    continue

                vu_dist = distances[v] + cost
                if u in distances:
                    # Negative or contradictory paths found
                    if vu_dist < distances[u]:
                        pass
                elif u not in visited or vu_dist < visited[u]:
                    visited[u] = vu_dist
                    push(queue, (vu_dist, next(c), u))
                    paths[u] = paths[v] + [u]

        return paths[dest_node]

    def dijkstra(self, graph, start_node, dest_node, limit, mode):
        if mode == "max":
            return self.maximum_elevation(graph, start_node, dest_node, limit, self.get_shortest_path)
        elif mode == "min":
            return self.minimum_elevation(graph, start_node, dest_node, limit, self.get_shortest_path)
        else:
            return self.get_shortest_path(graph, start_node, dest_node)
