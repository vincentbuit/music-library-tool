def process_tracknumber_title(tracknumber, title, artist_log, album_log):
    """
    Checks if all tracknumber and title meta-data is consistent and processes it to the desired format.
    :param tracknumber: List of all tracknumber meta-data from an album. Works for # or #/#
    :param title: List of all title meta-data from an album.
    :param artist_log: The current artist folder name. Used to generate print statements when an error occurs.
    :param album_log: The current album folder name. Used to generate print statements when an error occurs.
    :return: Two lists containing strings with the corrected meta-data.
    It return False if this meta-data is not consistent with eachother or itself, within an album.
    """
    corrected_tracknumbers = []
    corrected_titles = []
    bad_character = ['<', '>', ':', '"', '/', "\\", '|', '?', '*']
    # Check if the tracknumber and title meta-data is consistent with each other
    if len(tracknumber) != len(title):
        print(str(artist_log) + ' - ' + str(album_log) + ': Meta-data of titles is inconsistent with tracknumbers.')
        return False
    # Process the tracknumbers to the right format. Check if the tracknumber meta-data exists for every track
    for i in range(len(tracknumber)):
        if tracknumber[i] is not None:
            if tracknumber[i][0] == '0':
                # If the tracknumber starts with a '0', remove the '0'
                tracknumber[i] = tracknumber[i][1:]
            try:
                find_slash = tracknumber[i].index('/')
                new_tracknumber = tracknumber[i][0:find_slash]
                corrected_tracknumbers.append(new_tracknumber)
            except ValueError:
                corrected_tracknumbers.append(tracknumber[i])
        else:
            print(str(artist_log) + ' - ' + str(album_log) + ': Atleast 1 track without tracknumber meta-data.')
            return False
    # Process the titles to the right format. Check if the title meta-data exists for every track
    for j in range(len(title)):
        current_title = title[j]
        if current_title is None:
            print(str(artist) + ' - ' + str(album_log) + ': Atleast 1 track without title meta-data.')
            return False
        # Check for bad characters and remove if present
        for bad_c in bad_character:
            while True:
                try:
                    location_bad_c = current_title.index(bad_c)
                    current_title = current_title[:location_bad_c] + current_title[location_bad_c + 1:]
                except ValueError:
                    break
        corrected_titles.append(current_title)
    return corrected_tracknumbers, corrected_titles
