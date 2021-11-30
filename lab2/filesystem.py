import io

from binary_file import BinaryFile
from buffer_file import BufferFile
from directory import Directory
from text_file import TextFile


class FileSystem:
    def __init__(self):
        self.root = Directory("root")
        self.directories = {"root": self.root}
        self.files = {}

    def create_directory(self, dir_name):
        parent_dir_name = dir_name.split('\\')[-2]
        parent = self.directories[parent_dir_name]
        new_dir = parent.add_subdir(dir_name)
        if new_dir:
            self.directories[dir_name] = new_dir
        else:
            raise ValueError("directory can't have more than 10 elements")

    def delete_directory(self, dir_name):
        parent_dir_name = dir_name.split('\\')[-2]
        parent = self.directories[parent_dir_name]
        if parent.delete_subdir(dir_name):
            self.directories.pop(dir_name)

    def ls(self, dir_name):
        dir = self.directories[dir_name]
        subdirs = dir.list_subdirs()
        files = dir.list_files()
        print("Subdirectories: ")
        print(subdirs)
        print("Files: ")
        print(files)

    def move(self, node_name, dest):
        parent_dir_name = node_name.split('\\')[-2]
        short_name = node_name.split('\\')[-1]
        parent = self.directories[parent_dir_name]
        if parent.delete_subdir(node_name):
            self.directories.pop(node_name)
            dir_name = dest + "\\" + short_name
            new_dir = parent.add_subdir(dir_name)
            if new_dir:
                self.directories[dir_name] = new_dir
            else:
                raise ValueError("directory can't have more than 10 elements")
        else:
            file = self.files[node_name]
            if parent.delete_file(node_name):
                self.files.pop(node_name)
                file_name = dest + "\\" + short_name
                success = parent.add_file(file)
                if success:
                    self.files[file_name] = file
                else:
                    raise ValueError("directory can't have more than 10 elements")

    def create_binary_file(self, name):
        content = io.BytesIO(b'test')
        file = BinaryFile(name, content)
        parent_dir_name = name.split('\\')[-2]
        parent = self.directories[parent_dir_name]
        success = parent.add_file(file)
        if success:
            self.files[name] = file
        else:
            raise ValueError("directory can't have more than 10 elements")

    def read_file(self, name):
        file = self.files[name]
        return file.read()

    def create_text_file(self, name):
        content = io.StringIO()
        file = TextFile(name, content)
        parent_dir_name = name.split('\\')[-2]
        parent = self.directories[parent_dir_name]
        success = parent.add_file(file)
        if success:
            self.files[name] = file
        else:
            raise ValueError("directory can't have more than 10 elements")

    def write_text_file(self, name, line):
        file = self.files[name]
        file.write(line)

    def create_buffer_file(self, name):
        file = BufferFile(name)
        parent_dir_name = name.split('\\')[-2]
        parent = self.directories[parent_dir_name]
        success = parent.add_file(file)
        if success:
            self.files[name] = file
        else:
            raise ValueError("directory can't have more than 10 elements")

    def push_buffer_file(self, name, element):
        file = self.files[name]
        success = file.push(element)
        if not success:
            raise ValueError("buffer file can't have more than 10 elements")

    def pop_buffer_file(self, name):
        file = self.files[name]
        element = file.pop()
        return element

    def delete_file(self, name):
        parent_dir_name = name.split('\\')[-2]
        parent = self.directories[parent_dir_name]
        if parent.delete_file(name):
            self.files.pop(name)