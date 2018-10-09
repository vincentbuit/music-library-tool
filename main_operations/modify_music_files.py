from process_track_name import process_track_name
from meta_data_modify import meta_data_modify
from file_move_rename import file_move_rename


def modify_music_files(music_files, artist_proc, album_proc, date_proc, tracknumber_proc, title_proc, title):
    """
    Modifies the file names and meta-data for the provided music files.
    :param music_files: A list of path strings for the location of the music files it needs to process.
    :param artist_proc: A string of the artist name that will be used in the new track name and meta-data.
    :param album_proc: A string of the album name that will be used in the track name and meta-data.
    :param date_proc: A string of the date that will be used in the new track name and meta-data.
    :param tracknumber_proc: A list of strings of the tracknumbers that will be used
    in the new track name and meta-data.
    :param title_proc: A list of strings of the titles (based on processed meta-data) that will be used
    in the new track name but NOT in the meta-data.
    :param title: A list of strings of the titles (based on unprocessed meta-data) that will be used
    in the new meta-data. This is required because sometimes meta-data contains special characters which cannot be
    included in file names.
    """
    for i in range(0, len(music_files)):
        new_file_name = process_track_name(tracknumber_proc[i], artist_proc, title_proc[i])
        meta_data_modify(music_files[i], tracknumber_proc[i], artist_proc, title[i], album_proc, date_proc)
        file_move_rename(music_files[i], new_file_name)
