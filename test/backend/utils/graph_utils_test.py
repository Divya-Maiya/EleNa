import os
import unittest
from mockito import *
import osmnx
import pickle
import networkx

from src.backend.utils.map_utils import *
from src.backend.utils.graph_utils import *
from src.backend.model.model import *


def test_setup():
    os.chdir("../..")
    return load_map("resources/graph_Amherst.pkl", changeDir=1)


graph = test_setup()


class testGraphUtils(unittest.TestCase):
    global graph

    def test_shortest_path_optimizer(self):
        source_node = 66692331
        successor_graph = graph._succ if graph.is_directed() else graph._adj
        expected_coords = -72.532612, 42.406836
        when(osmnx).nearest_nodes(...).thenReturn((source_node, 0))
        when(osmnx).geocode(...).thenReturn(expected_coords)

        source_node = get_node_from_address(graph, "Random String")
        neighbor = 66644252
        w = successor_graph[source_node][66644252]

        def weight_(source, dest, edge_data):
            return min(attr.get('length', 1) for attr in edge_data.values())

        expected_function = weight_
        obtained_function = shortest_path_optimizer(graph, 'length')
        self.assertEqual(obtained_function(source_node, neighbor, w), expected_function(source_node,neighbor,w))
        unstub()

        # clean up


    def test_get_map(self):

        when(osmnx).graph_from_place(...).thenReturn(graph)
        when(osmnx).add_node_elevations_google(...).thenReturn(graph)
        when(osmnx).add_edge_grades(...).thenReturn(graph)

        when(pickle).dump(...)
        # when(pickle).dump(...).thenReturn()

        get_map("Amherst", "Massachusetts", "USA", "abc", "testFile")

        verify(osmnx, times=1).graph_from_place(...)
        verify(osmnx, times=1).add_node_elevations_google(...)
        verify(osmnx, times=1).add_edge_grades(...)
        verify(pickle, times=1).dump(...)

        unstub()

    def test_get_node_from_address(self):
        address = "1 Rolling Green Dr, Amherst, MA 01002"

        expected_node = 66737929
        obtained_node = get_node_from_address(graph, address)

        self.assertEqual(expected_node, obtained_node)

        unstub()


if __name__ == '__main__':
    unittest.main()
