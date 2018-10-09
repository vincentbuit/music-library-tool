from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC


def meta_data_modify(file_location, tracknumber, artist, title, album, date):
    """
    Modify the meta data of a music file to the given input.
    :param file_location: The path of the file to be modified.
    :return: Returns false if given input is not a music file.
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
        return False
    # Modify the meta-data
    audio_file['artist'] = artist
    audio_file['title'] = title
    audio_file['album'] = album
    audio_file['tracknumber'] = tracknumber
    audio_file['date'] = date
    audio_file.save()
