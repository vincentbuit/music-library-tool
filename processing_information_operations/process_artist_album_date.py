def process_artist_album_date(artist, album, date, artist_log, album_log):
    """
    Checks if all artist, album and date meta-data is consistent from an album and returns a single string for all
    meta-data variables.
    :param artist: List of all artist meta-data from an album.
    :param album: List of all artist meta-data from an album.
    :param date: List of all date meta-data from an album.
    :param artist_log: The current artist folder name. Used to generate print statements when an error occurs.
    :param album_log: The current album folder name. Used to generate print statements when an error occurs.
    :return: Three strings with the corrected meta-data.
    It return False if this meta-data is not consistent with eachother or itself, within an album.
    """
    artist_final = None
    album_final = None
    date_final = None
    bad_character = ['<', '>', ':', '"', '/', "\\", '|', '?', '*']
    # Check if the artist, album and date meta-data is consistent with each other
    if len(artist) != len(album) != len(date):
        print(str(artist_log) + ' - ' + str(
            album_log) + ': Meta-data of artist, album and date is inconsistent with each other.')
        return False
    # Shorten the lists to a single string value. Return False and log if some meta-data is inconsistent
    for i in range(len(artist)):
        if artist[i] is not None:
            if i == 0 or artist_final is None:
                artist_final = artist[i]
            # Check if the artist meta-data is consistent with itself
            elif artist[i] != artist_final:
                print(str(artist_log) + ' - ' + str(album_log) + ': Artist meta-data is inconsistent with itself.')
                return False
            artist_final = artist[i]
    for i in range(len(album)):
        if album[i] is not None:
            if i == 0 or album_final is None:
                album_final = album[i]
            # Check if the album meta-data is consistent with itself
            elif album[i] != album_final:
                print(str(artist_log) + ' - ' + str(album_log) + ': Album meta-data is inconsistent with itself.')
                return False
            album_final = album[i]
    for i in range(len(date)):
        if date[i] is not None:
            if i == 0 or date_final is None:
                date_final = date[i]
            # Check if the date meta-data is consistent with itself
            elif date[i] != date_final:
                print(str(artist_log) + ' - ' + str(album_log) + ': Date meta-data is inconsistent with itself.')
                return False
            date_final = date[i]
    # Check if the minimum required meta data exists
    if artist_final is None or album_final is None or date_final is None:
        print(str(artist_log) + ' - ' + str(album_log) + ': There is no meta-data for artist, album or date.')
        return False
    # Check for bad characters and remove if present
    for bad_c in bad_character:
        while True:
            try:
                location_bad_c = artist_final.index(bad_c)
                artist_final = artist_final[:location_bad_c] + artist_final[location_bad_c + 1:]
            except ValueError:
                break
        while True:
            try:
                location_bad_c = album_final.index(bad_c)
                album_final = album_final[:location_bad_c] + album_final[location_bad_c + 1:]
            except ValueError:
                break
        while True:
            try:
                location_bad_c = date_final.index(bad_c)
                date_final = date_final[:location_bad_c] + date_final[location_bad_c + 1:]
            except ValueError:
                break
    return [artist_final, album_final, date_final]
