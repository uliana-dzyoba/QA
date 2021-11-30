class TextFile:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def read(self):
        return self.content.getvalue()

    def write(self, line):
        print(line, end=" ", file=self.content)