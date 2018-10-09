from config import number_style_1, number_style_2, number_style_3, include_artist_name


def process_track_name(tracknumber, artist, title):
    """
    Using the input and the config file, this functions generates a string with the new file name.
    :param tracknumber: The number of the track on the album.
    :param artist: The artist of the track
    :param title: The title of the track.
    :return: A string containing the new file name.
    """
    # Use the appropriate lay-out configuration from the config file
    if int(tracknumber) < 10:
        tracknumber = '0' + tracknumber
    if number_style_1 is True:
        trackname = tracknumber + ' '
    elif number_style_2 is True:
        trackname = tracknumber + '. '
    elif number_style_3 is True:
        trackname = tracknumber + ' - '

    else:
        print('No tracknumber style has been selected in the config file.')
        return False
    if include_artist_name is True:
        trackname += artist + ' - '
    trackname += title
    return trackname
