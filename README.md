Music Library Tool
------------------
This tool will process and organize your music to your music library. It will make sure that all file names, folder names and meta-data have a consistent style.
You start by opening the config file and filling in the path to your music library location and the path to your new music location (make sure your new music is in here as well).
Next you can configure the desired lay-out options of the processed music. 
Make sure your new music folder follows the following structure: `New_music_folder/Artist_folder/Album_folder/*NEW MUSIC*`

When that's all finished, `loop_through_new_music.py`, located in the `main_operations folder`, should be executed. It will print anything which it cannot process including the error.

At the moment it doesn't support other music file types than MP3 and FLAC.
