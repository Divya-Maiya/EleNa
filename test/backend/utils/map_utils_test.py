import os
import unittest
from mockito import when, mock, unstub, verify
import osmnx
import pickle
from src.backend.utils.map_utils import *


class MyTestCase(unittest.TestCase):
    def test_get_geocode(self):
        expected_coordinates = (42.362465, -72.485407)

        response = (42.362465, -72.485407)
        when(osmnx).geocode(...).thenReturn(response)

        obtained_coordinates = get_coordinates("1 Rolling Green Dr, Amherst, MA 01002")
        self.assertEqual(obtained_coordinates, expected_coordinates)

        verify(osmnx, times=1).geocode(...)

        # clean up
        unstub()

    def test_get_map(self):
        os.chdir("../..")
        graph = load_map("resources/graph_Amherst.pkl", changeDir=1)

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
        os.chdir("../..")
        graph = load_map("resources/graph_Amherst.pkl", changeDir=1)

        address = "1 Rolling Green Dr, Amherst, MA 01002"

        expected_node = 66737929
        obtained_node = get_node_from_address(graph, address)

        self.assertEqual(expected_node, obtained_node)

        unstub()


if __name__ == '__main__':
    unittest.main()