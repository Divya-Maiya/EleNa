
def weight_function(graph, weight='length'):
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
    for i in range(len(path)-1):
        length += graph[path[i]][path[i+1]][0]['length']
    return length

