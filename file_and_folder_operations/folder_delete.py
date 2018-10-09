import os


def folder_delete(path):
    """
    Deletes the folder specified by path. Use in combination with folder_is_empty.
    :param path: The destination of the folder that needs to be deleted.
    """
    os.rmdir(path)
