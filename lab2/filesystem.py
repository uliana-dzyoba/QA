from directory import Directory

class FileSystem:
    def __init__(self):
        self.root = Directory("root")
        self.directories = {"root": self.root}

    def create_directory(self, dir_name):
        pass

    def delete_directory(self, dir_name):
        pass

    def ls(self, dir_name):
        pass

    def move(self, node_name, dest):
        pass

    def create_binary_file(self, file_name):
        pass

    def create_text_file(self, file_name):
        pass

    def write_text_file(self, file_name):
        pass

    def create_buffer_file(self, file_name):
        pass

    def push_buffer_file(self, file_name):
        pass

    def pop_buffer_file(self, file_name):
        pass

    def delete_file(self, file_name):
        pass