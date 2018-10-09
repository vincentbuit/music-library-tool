import os
import shutil


def file_move_rename(file_location, name_new=None, new_direction=None):
    """
    Rename file. If new_direction is provided then it will also move the file. Note the the new directory must already
    exist!
    :param file_location: file location as a string including suffix.
    :param name_new: the new file name as a string. No suffix is needed.
    :param new_direction: the new location of the file (string).
    """
    # Get the filename from the location
    file_index = file_location.rfind('/')
    file_name_current = file_location[file_index + 1:]
    file_path_current = file_location[:file_index]
    # Get file suffix
    find_dot = file_name_current.rfind('.')
    file_name_suffix = file_name_current[find_dot + 1:]
    # Check if new name is provided. If so, change the file name
    if name_new is None:
        new_file_name = file_name_current
    else:
        new_file_name = name_new + '.' + file_name_suffix
    # Check if new directory is provided. If so, change the directory
    if new_direction is None:
        new_direction_path = file_path_current
    else:
        new_direction_path = new_direction
    # Rename and move the file
    shutil.move(file_location, os.path.join(new_direction_path, new_file_name))
