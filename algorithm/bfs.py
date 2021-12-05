from utils import graph_utils


def bfs(graph, start_node, dest_node, limit, mode):
    if mode == "max":
        return maximum_elevation(graph, start_node, dest_node, limit)
    else:
        return minimum_elevation(graph, start_node, dest_node, limit)

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

    def maximum_elevation(self, source, goal):
        """Gets the shortest path within a path length limit, optimizing for maximum elevation.
        Parameters
        ----------
        source : node
            starting point node for the path
        goal : node
            destination node for the path
        Returns
        ------
        list of nodes that form the discovered path
        """

        # print("calling maximizing elevation")
        graph = self.graph

        shortest_path = self.vanilla_shortest_path(source, goal)
        shortest_path_length = graph_utils.get_path_length(graph, shortest_path)
        max_path_length = shortest_path_length * (1 + self.limit)
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
                path_elevation = graph_utils.get_path_elevation(graph, path)
                path_length = graph_utils.get_path_length(graph, path)

                if path_elevation > highest_elevation:
                    if path_length <= allowance + min_distance:
                        highest_elevation = path_elevation
                        best_path = path

            best_path_length = graph_utils.get_path_length(graph, best_path)
            length_allowance -= (best_path_length - min_distance)

            for j in best_path[:-1]:
                max_path.append(j)
        max_path.append(goal)
        return max_path
