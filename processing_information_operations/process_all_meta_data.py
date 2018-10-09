from meta_data_get import meta_data_get
from process_tracknumber_title import process_tracknumber_title
from process_artist_album_date import process_artist_album_date


def process_all_meta_data(music_files, artist_log, album_log):
    """
    Processes the meta-data of an entire album of music files according to the config file.
    :param music_files: A list of path strings for the location of the music files it needs to process.
    :param artist_log: The current artist folder name. Used to generate print statements when an error occurs.
    :param album_log: The current album folder name. Used to generate print statements when an error occurs.
    :return: Returns processed meta-data: Artist, album, date, tracknumber and title.
    Returns unprocessed meta-data title as well. This is required because sometimes meta-data contains special
    characters which cannot be included in file names.
    """
    tracknumber = []
    artist = []
    title = []
    album = []
    date = []
    # Get all the meta-data and organize it in lists
    for file in music_files:
        meta_data = meta_data_get(file, artist_log, album_log)  # [tracknumber, artist, title, album, date]
        tracknumber.append(meta_data[0])
        artist.append(meta_data[1])
        title.append(meta_data[2])
        album.append(meta_data[3])
        date.append(meta_data[4])
    # Process all the meta-data
    processed_tracknumber_title = process_tracknumber_title(tracknumber, title, artist_log, album_log)
    processed_artist_album_date = process_artist_album_date(artist, album, date, artist_log, album_log)
    if processed_tracknumber_title is False or processed_artist_album_date is False:
        return False
    # Organize the processed meta data
    tracknumber_proc = processed_tracknumber_title[0]  # List
    artist_proc = processed_artist_album_date[0]  # String
    title_proc = processed_tracknumber_title[1]  # List
    album_proc = processed_artist_album_date[1]  # String
    date_proc = processed_artist_album_date[2]  # String
    # Return the processed meta data and some unprocessed meta data for later use
    return [artist_proc, album_proc, date_proc, tracknumber_proc, title_proc, title]
