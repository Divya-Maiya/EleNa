import heapq
from abc import ABC
from itertools import count

from src.backend.algorithm.algorithm import *
from src.backend.utils.graph_utils import *

"""
To get the shortest path using the A* Algorithm
"""


class AStar(Algorithm):
    def get_shortest_path(self, graph, start_node, dest_node, edge_weight='length'):
        push = heapq.heappush
        pop = heapq.heappop

        successor_graph = graph._succ if graph.is_directed() else graph._adj

        weight = shortest_path_optimizer(graph, edge_weight)
        c = count()
        queue = [(0, next(c), start_node, 0, None)]

        enqueued = {}
        explored = {}

        while queue:
            _, __, curnode, dist, parent = pop(queue)

            if curnode == dest_node:
                path = [curnode]
                node = parent
                while node is not None:
                    path.append(node)
                    node = explored[node]
                path.reverse()
                return path

            if curnode in explored:
                if explored[curnode] is None:
                    continue

                qcost, h = enqueued[curnode]
                if qcost < dist:
                    continue

            explored[curnode] = parent

            if curnode not in successor_graph:
                raise Exception("Start node is not in the map. Please restart with the correct start node")

            for neighbor, w in successor_graph[curnode].items():
                ncost = dist + weight(curnode, neighbor, w)
                if neighbor in enqueued:
                    qcost, h = enqueued[neighbor]
                    if qcost <= ncost:
                        continue
                else:
                    h = get_l1_distance(graph, neighbor, dest_node)
                enqueued[neighbor] = ncost, h
                push(queue, (ncost + h, next(c), neighbor, ncost, curnode))

    def astar(self, graph, start_node, dest_node, limit, mode):
        if mode == "max":
            return self.maximum_elevation(graph, start_node, dest_node, limit, self.get_shortest_path)
        elif mode == "min":
            return self.minimum_elevation(graph, start_node, dest_node, limit, self.get_shortest_path)
        else:
            return self.get_shortest_path(graph, start_node, dest_node)
