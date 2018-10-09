from config import library_location, music_location, include_release_year
from folder_get_inside import folder_get_inside
from folder_delete import folder_delete
from process_all_meta_data import process_all_meta_data
from modify_music_files import modify_music_files
from folder_move_rename import folder_move_rename
from folder_is_empty import folder_is_empty
from get_artist_or_album_name import get_artist_or_album_name
import os


def loop_through_new_music():
    """
    This is the main script. It will scan the specified folder (config file) for new music. It will process the
    meta-data, file names and folder names according to the config file. Afterwards it will move the processed music to
    the correct location in the specified music library location. If it was unable to process certain music it will
    print the reason why it was unable to process this music.
    """
    all_new_artists = folder_get_inside(music_location)[0]
    library_artists = folder_get_inside(library_location)[0]
    # If the new music folder is empty the script is finished
    if len(all_new_artists[0]) == 0:
        print('No folders were found inside the new music folder')
        return
    # Loop through all new artists
    for new_artist in all_new_artists:
        artist_log = get_artist_or_album_name(new_artist)
        # Find all albums inside a new artist folder
        all_new_albums = folder_get_inside(new_artist)[0]
        # If no album is inside the artist folder then delete the folder if it's empty or log if it's not empty
        if len(all_new_albums) == 0:
            if folder_is_empty(new_artist):
                folder_delete(new_artist)
                print('The artist folder ' + str(artist_log) + ' is empty and therefor it has been deleted')
            else:
                print('The artist folder ' + str(artist_log) + ' doesn\'t contain any albums but contains other files.')
                break
        # Process all the music files inside the album folder and move the album or artist folder afterwards
        for new_album in all_new_albums:
            album_log = get_artist_or_album_name(new_album)
            # Get all music files
            all_new_music = folder_get_inside(new_album)[1]
            # Test if there are no music files inside the album folder. Probably there are more folders (like CD1/CD2),
            # these cases are unsolved for now
            if not all_new_music:
                print(str(artist_log) + ' - ' + str(
                    album_log) + ': There is no music inside the album folder. Chances are there are folders '
                                 'inside the ' + str(album_log) + ' folder containing the music. '
                                                                  'This is currently not supported.')
                break
            # Get and process all meta data
            all_meta_data = process_all_meta_data(all_new_music, artist_log, album_log)
            # Only continue if there are no inconsistencies or empty fields in the meta-data
            if all_meta_data is not False:
                # Check if the artist already exists in the music library
                check_artist_library_path = os.path.join(library_location, all_meta_data[0])
                if check_artist_library_path in library_artists:
                    # The artist exists in the library, get all albums of current artist inside the library
                    library_albums = folder_get_inside(check_artist_library_path)[0]
                    # Check if current album is already in the library, taking album name config into account
                    check_album_library_path1 = os.path.join(check_artist_library_path, all_meta_data[1])
                    check_album_library_path2 = os.path.join(check_artist_library_path,
                                                             all_meta_data[1] + ' (' + all_meta_data[2] + ')')
                    if check_album_library_path1 in library_albums or check_album_library_path2 in library_albums:
                        # The album already exists in the library. Break the current iteration
                        print(str(artist_log) + ' - ' + str(album_log) + ': Already exists in the library.')
                        break
                    # The album doesn't exist in the library. Define the new album location inside the library
                    new_album_location = os.path.join(library_location, all_meta_data[0])
                    # Generate the new album name based on the config file
                    if include_release_year is True:
                        new_album_name = all_meta_data[1] + ' (' + all_meta_data[2] + ')'
                    else:
                        new_album_name = all_meta_data[1]
                    # Modify the music files (change file names and update meta-data)
                    modify_music_files(all_new_music, all_meta_data[0], all_meta_data[1], all_meta_data[2],
                                       all_meta_data[3], all_meta_data[4], all_meta_data[5])
                    # Rename and move the current album to the library
                    folder_move_rename(new_album, new_album_name, new_album_location)
                    # Delete the artist folder if it's empty
                    if folder_is_empty(new_artist):
                        folder_delete(new_artist)
                # The artist doesn't exist in the library
                else:
                    # Modify the music files (change file names and update meta-data)
                    modify_music_files(all_new_music, all_meta_data[0], all_meta_data[1], all_meta_data[2],
                                       all_meta_data[3], all_meta_data[4], all_meta_data[5])
                    # Generate the new album name based on the config file
                    if include_release_year is True:
                        new_album_name = all_meta_data[1] + ' (' + all_meta_data[2] + ')'
                    else:
                        new_album_name = all_meta_data[1]
                    # Rename the album
                    folder_move_rename(new_album, new_album_name)
                    # Move and rename the artist if the current album is the last album of the current artist from new music
                    if new_album == all_new_albums[-1]:
                        new_artist_name = all_meta_data[0]
                        folder_move_rename(new_artist, new_artist_name, library_location)


loop_through_new_music()
