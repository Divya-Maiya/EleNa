import unittest
from mockito import when, mock, unstub
import osmnx

from src.backend.utils.map_utils import get_coordinates


class MyTestCase(unittest.TestCase):
    def test_get_geocode(self):
        expected_coordinates = (42.362465, -72.485407)

        response = (42.362465, -72.485407)
        when(osmnx).geocode(...).thenReturn(response)

        obtained_coordinates = get_coordinates("1 Rolling Green Dr, Amherst, MA 01002")
        self.assertEqual(obtained_coordinates, expected_coordinates)

        # clean up
        unstub()


if __name__ == '__main__':
    unittest.main()
