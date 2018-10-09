import os
import shutil


def folder_move_rename(folder_location, name_new=None, new_direction=None):
    """
    Rename folder. If new_direction is provided than it will also move the folder. Note the the new directory
    must already exist!
    :param folder_location: folder location as a string.
    :param name_new: the new folder name as a string.
    :param new_direction: the new location of the folder (string).
    """
    # Get the folder name from the location. Find out whether it comes after a / or \\
    forward_slash = folder_location.rfind('/')
    backward_slash = folder_location.rfind('\\')
    if forward_slash > backward_slash:
        folder_index = folder_location.rfind('/')
    else:
        folder_index = folder_location.rfind('\\')
    folder_name_current = folder_location[folder_index + 1:]
    # Check if a new name is provided. If so, change the folder name
    if name_new is None:
        new_folder_name = folder_name_current
    else:
        new_folder_name = name_new
    # Check if new directory is provided. If so, change the directory
    if new_direction is None:
        new_direction_path = folder_location[:folder_index + 1]
    else:
        new_direction_path = new_direction
    path_new = os.path.join(new_direction_path, new_folder_name)
    # Move and rename the folder
    shutil.move(folder_location, path_new)
