import os
import unittest
from mockito import *
import osmnx
import pickle

from src.backend.utils.map_utils import *
from test.helper_utils import test_setup

graph = test_setup()


class MyTestCase(unittest.TestCase):
    global graph

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

        when(osmnx).graph_from_place(...).thenReturn(graph)
        when(osmnx).add_node_elevations_google(...).thenReturn(graph)
        when(osmnx).add_edge_grades(...).thenReturn(graph)

        when(pickle).dump(...)
        # when(pickle).dump(...).thenReturn()

        os.chdir("../src")
        print(os.getcwd())
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
