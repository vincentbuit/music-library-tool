def get_artist_or_album_name(folder_location):
    """
    Returns the last folder name from the provided path for error displaying purposes.
    :param folder_location: A string of the folder path.
    :return: The last folder name from the folder path.
    """
    # Get the folder name from the location. Find out whether it comes after a / or \\
    forward_slash = folder_location.rfind('/')
    backward_slash = folder_location.rfind('\\')
    if forward_slash > backward_slash:
        folder_index = folder_location.rfind('/')
    else:
        folder_index = folder_location.rfind('\\')
    folder_name_current = folder_location[folder_index + 1:]
    return folder_name_current
