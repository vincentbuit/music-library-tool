import os
from os import listdir
from os.path import isfile, join


def folder_get_inside(location):
    """
    Get everything inside a location as a list of string paths sorted in folders, music files and other files.
    :param location: complete string of directory.
    :return: tuple of lists of folders, music_files and other_files.
    """
    # Get all files inside the provided location
    all_files = [f for f in listdir(location) if isfile(join(location, f))]
    music_files = []
    other_files = []
    # Filter out all the music files and put them in a list
    for f in all_files:
        if f[f.rfind('.') + 1:] == 'flac' or f[f.rfind('.') + 1:] == 'mp3':
            music_files.append(location + '/' + f)
    # Filter out all the other files and put them in a list as well
    for f in all_files:
        if (location + '/' + f) not in music_files:
            other_files.append(location + '/' + f)
    # Get all folders inside the provided location
    folders = [os.path.join(location, o) for o in os.listdir(location) if os.path.isdir(os.path.join(location, o))]
    return folders, music_files, other_files
