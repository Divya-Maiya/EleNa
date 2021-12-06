from abc import ABC

from src.backend.algorithm.algorithm import Algorithm


class BFS(Algorithm, ABC):
    def get_shortest_path(self, graph, start_node, dest_node, edge_weight='length'):
        explored = []

        # start the BFS queue
        queue = [[start_node]]

        # return if start node is the end node
        if start_node == dest_node:
            return [dest_node]

        # keeps looping until all possible paths have been checked
        while queue:
            path = queue.pop(0)
            node = path[-1]
            # add neighboring nodes if they haven't been explored
            if node not in explored:
                neighbors = graph.neighbors(node)
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                    if neighbor == dest_node:
                        return new_path
                explored.append(node)
        # Return empty list if path doesn't exist
        return []

    def bfs(self, graph, start_node, dest_node, limit, mode):
        return self.get_shortest_path(self, graph, start_node, dest_node)
