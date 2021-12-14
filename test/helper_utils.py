from src.backend.utils.map_utils import load_map


def test_setup():
    return load_map("resources/graph_Amherst.pkl", changeDir=1)