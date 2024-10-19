#!/usr/bin/env python3

import os

def rename_images(folder_path, prefix):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    # Sort the files to ensure consistent renaming order
    files.sort()
    
    # Iterate over the files and rename them
    for i, filename in enumerate(files):
        # Create the new filename with the prefix and index
        new_filename = f"{prefix}{i+1}.jpg"
        # Get the full path of the old and new file
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed {old_file} to {new_file}")

# Define the folder path and prefix//media/beki/My Passport/research/unannotated/happy
folder_path = os.path.expanduser('/media/beki/My Passport/new data/angry/')
prefix = "angryy"

# Call the function to rename the images
rename_images(folder_path, prefix)
