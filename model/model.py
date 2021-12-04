"""
Defining the model
"""


class Model(object):

    def _init_(self):
        # self.modes = ['minimize', 'maximize']
        self.source = None
        self.destination = None
        self.limit = None
        self.mode = None
        # self.graph_projection = None
        self.algorithm = None
        # self.bbox = None
        # self.impedence = None
        # self.key = None

    # setters
    def set_source(self, s):
        self.source = s

    def set_destination(self, d):
        self.destination = d

    def set_mode(self, mode):
        self.mode = mode

    def set_limit(self, o):
        self.limit = o

    def set_algorithm(self, algorithm):
        self.algorithm = algorithm

    # def set_bbox(self, bb):
    #     self.bbox = bb
    #
    # def set_graph_projection(self, graph_projection):
    #     self.graph_projection = graph_projection
    #
    # def set_key(self, key):
    #     self.key = key

    # getters

    # def get_graph_projection(self):
    #     return self.graph_projection

    def get_source(self):
        return self.source

    def get_destination(self):
        return self.destination

    def get_mode(self):
        return self.mode

    def get_limit(self):
        return self.limit

    def get_algorithm(self):
        return self.algorithm

    # def get_bbox(self):
    #     return self.bbox
    #
    # def get_key(self):
    #     return self.key
