from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC


# It returns an error if the file parsed does not exist!
def meta_data_get(file_location, artist_log, album_log):
    """
    Get's all the relevant meta-data from an audio file and returns a list.
    :param file_location: The current location of the file (string).
    :param artist_log: The current artist folder name. Used to generate print statements when an error occurs.
    :param album_log: The current album folder name. Used to generate print statements when an error occurs.
    :return: a list of strings containing all the meta data from a file. False if audio format is not supported.
    It puts None if no meta-data is there.
    """
    # Get the filename from the location
    file_index = file_location.rfind('/')
    file_name_current = file_location[file_index + 1:]
    # Get the file suffix
    find_dot = file_name_current.rfind('.')
    file_name_suffix = file_name_current[find_dot + 1:]
    # Read the file
    if file_name_suffix == 'mp3':
        audio_file = EasyID3(file_location)
    elif file_name_suffix == 'flac':
        audio_file = FLAC(file_location)
    else:
        print(str(artist_log) + ' - ' + str(album_log) + ': File type ' + str(file_name_suffix) + ' is not supported.')
        return False
    try:
        artist = ''.join(audio_file['artist'])
    except KeyError:
        artist = None
    try:
        title = ''.join(audio_file['title'])
    except KeyError:
        title = None
    try:
        album = ''.join(audio_file['album'])
    except KeyError:
        album = None
    try:
        tracknumber = ''.join(audio_file['tracknumber'])
    except KeyError:
        tracknumber = None
    try:
        date = ''.join(audio_file['date'])
    except KeyError:
        date = None
    return [tracknumber, artist, title, album, date]
