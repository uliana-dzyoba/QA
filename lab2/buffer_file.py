class BufferFile:
    MAX_BUF_FILE_SIZE = 10
    def __init__(self, name):
        self.name = name
        self.elements = []

    def push(self, element):
        if len(self.elements) < self.MAX_BUF_FILE_SIZE:
            self.elements.append(element)
            return True
        else:
            return False

    def pop(self):
        self.elements.pop(0)