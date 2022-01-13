import pytest

from buffer_file import BufferFile
from directory import Directory
from filesystem import FileSystem


@pytest.fixture
def fs():
    return FileSystem()


def test_create_directory(fs):
    fs.create_directory("root\\test_create")
    assert fs.directories.get("root\\test_create") != None

def test_create_directory_max(fs):
    Directory.DIR_MAX_ELEMS = 1
    fs.create_directory("root\\test_create_max_1")
    fs.create_directory("root\\test_create_max_2")
    assert False


def test_delete_directory(fs):
    fs.create_directory("root\\test_delete")
    fs.delete_directory("root\\test_delete")
    assert fs.directories.get("root\\test_delete") == None


# def test_ls():
#     assert True


def test_move_dir(fs):
    fs.create_directory("root\\test_move1")
    fs.create_directory("root\\test_move2")
    fs.move("root\\test_move2", "root\\test_move1")
    assert fs.directories.get("root\\test_move1\\test_move2") != None

def test_move_file(fs):
    fs.create_directory("root\\test_move3")
    fs.create_text_file("root\\test_move4")
    fs.move("root\\test_move4", "root\\test_move3")
    assert fs.files.get("root\\test_move3\\test_move4") != None


def test_create_binary_file(fs):
    fs.create_binary_file("root\\binary_test")
    assert fs.files.get("root\\binary_test") != None


def test_create_text_file(fs):
    fs.create_text_file("root\\text_test")
    assert fs.files.get("root\\text_test") != None


def test_read_file(fs):
    fs.create_text_file("root\\read_test")
    fs.write_text_file("root\\read_test", "testing reading")
    assert fs.read_file("root\\read_test") == "testing reading"


def test_write_text_file(fs):
    fs.create_text_file("root\\write_test")
    fs.write_text_file("root\\write_test", "testing writing")
    assert fs.files.get("root\\write_test").content.getvalue() == "testing writing "


def test_create_buffer_file(fs):
    fs.create_buffer_file("root\\buffer_test")
    assert fs.files.get("root\\buffer_test") != None


def test_delete_file(fs):
    fs.create_text_file("root\\delete_test")
    fs.delete_file("root\\delete_test")
    assert fs.files.get("root\\delete_test") == None


def test_push_buffer_file(fs):
    fs.create_buffer_file("root\\push_test")
    fs.push_buffer_file("root\\push_test", "element1")
    assert fs.files.get("root\\push_test").elements[0] == "element1"

def test_push_buffer_file_max(fs):
    BufferFile.MAX_BUF_FILE_SIZE = 1
    fs.create_buffer_file("root\\push_max_test")
    fs.push_buffer_file("root\\push_max_test", "element1")
    fs.push_buffer_file("root\\push_max_test", "element2")
    assert False


def test_pop_buffer_file(fs):
    fs.create_buffer_file("root\\pop_test")
    fs.push_buffer_file("root\\pop_test", "element1")
    fs.pop_buffer_file("root\\pop_test")
    assert fs.files.get("root\\pop_test").elements == []
