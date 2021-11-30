class Directory:
    DIR_MAX_ELEMS = 10
    def __init__(self, name):
        self.name = name
        self.subdirs = {}
        self.files = {}

    def add_subdir(self, name):
        if len(self.subdirs) + len(self.files) < self.DIR_MAX_ELEMS:
            new_dir = Directory(name)
            self.subdirs[name] = new_dir
            return new_dir
        else:
            return False

    def add_file(self, file):
        if len(self.subdirs) + len(self.files) < self.DIR_MAX_ELEMS:
            self.files[file.name] = file
            return True
        else:
            return False

    def delete_subdir(self, name):
        return self.subdirs.pop(name, None)

    def delete_file(self, name):
        return self.files.pop(name, None)

    def list_subdirs(self):
        subdirs = []
        for key in self.subdir:
            subdirs.append(key)
        return subdirs

    def list_files(self):
        files = []
        for key in self.files:
            files.append(key)
        return files