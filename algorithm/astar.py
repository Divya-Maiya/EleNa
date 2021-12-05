import heapq
import map_utils
import networkx as nx
from itertools import count

from utils.graph_utils import *
from utils.map_utils import *


def astar(graph, start_node, dest_node, mode):
    push = heapq.heappush
    pop = heapq.heappop

    successor_graph = graph._succ if graph.is_directed() else graph._adj

    weight = graph_utils.shortest_path_optimizer(graph, mode)
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

        for neighbor, w in successor_graph[curnode].items():
            ncost = dist + weight(curnode, neighbor, w)
            if neighbor in enqueued:
                qcost, h = enqueued[neighbor]
                if qcost <= ncost:
                    continue
            else:
                h = (graph, neighbor, dest_node)
            enqueued[neighbor] = ncost, h
            push(queue, (ncost + h, next(c), neighbor, ncost, curnode))
    pass