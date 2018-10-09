import os


def folder_is_empty(path):
    """
    Check if a directory is empty.
    :param path: String of location path.
    :return: Boolean. True if empty.
    """
    if len(os.listdir(path)) == 0:
        return True
    else:
        return False
