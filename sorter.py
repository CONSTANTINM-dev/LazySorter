import os

# define the target directory for the sorting operation, does not os.walk
cwd = os.path.dirname(os.path.abspath(__file__))
target = target = os.path.dirname(cwd)

# makes an exploitable lists of all entities found in the target directory
scanlist = []

# furnishes the scanlist module to be able to sort off folders without ignoring them
with os.scandir(target) as explore:
    for entries in explore:
        scanlist.append(entries)

# files list to be worked through the mover.py module
files = []

# exists for counting purposes, no operation besides a print(len)
folders = []

# differenciates folders from files
folders = [entries for entries in scanlist if entries.is_dir()]
files = [entries for entries in scanlist if entries.is_file()]

# lists of folders to be created in the target directory
directories = ["sort_spreadsheets","sort_textfiles", "sort_archives","sort_images","sort_videos", "sort_audio", "sort_presentations", "sort_executables" , "sort_undetermined"]


# function to create folders in the current working directory, with error fallbacks
def createrelativedirs():
    if not files:
        print("No files to work with")
        return
    for directory in directories:
        try:
            os.mkdir(os.path.join(target,directory))
            print(f"{directory} folder created in {target}")
        except FileExistsError: 
            pass
        except PermissionError:
            print(f"Permission denied: Unable to create {directory} in {target}.")
        except Exception as e:
            print(f"An unexpected error occurred while creating {directory} in {target}: {e}")
    