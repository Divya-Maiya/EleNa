import unittest

from src.backend.model.model import Model


class TestModel(unittest.TestCase):
    def test_model_setters(self):
        mode = "max"
        source = "source"
        dest = "dest"
        limit = 50
        algorithm = "AStar"

        model = Model()
        model.set_mode(mode)
        model.set_limit(limit)
        model.set_source(source)
        model.set_destination(dest)
        model.set_algorithm(algorithm)

        # Assert all values
        self.assertEqual(model.get_mode(), mode)
        self.assertEqual(model.get_limit(), limit)
        self.assertEqual(model.get_source(), source)
        self.assertEqual(model.get_algorithm(), algorithm)
        self.assertEqual(model.get_destination(), dest)


if __name__ == '__main__':
    unittest.main()
