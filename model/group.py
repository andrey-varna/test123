class Group:
    def __init__(self, name=None, header=None, footer=None):
        self.name = name
        self.header = header
        self.footer = footer


class Rename:
    def __init__(self, name):
        self.name = name
