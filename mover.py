import shutil
import datetime
from sorter import *
from visualelem import *

# blank lists for files types
sort_spreadsheets = []
sort_textfiles = []
sort_archives = []
sort_images = []
sort_videos = []
sort_audio = []
sort_presentations = []
sort_executables = []
sort_undetermined = []
meta = {"sort_spreadsheets": sort_spreadsheets, "sort_textfiles": sort_textfiles, "sort_archives": sort_archives, "sort_images": sort_images, "sort_videos": sort_videos, "sort_audio" : sort_audio, "sort_presentations": sort_presentations, "sort_executables": sort_executables, "sort_undetermined": sort_undetermined}

# lists for log events
success_log = []
error_log = []
lost_log = []

# get timestamp for log purposes, format is YYMMDD_HMS
exectime = datetime.datetime.now()
getexectime = exectime.strftime("%Y%m%d_%H%M%S")+"_file_sort_log.txt"

# determines working location to generate logs
log_get_target = os.path.join(target, getexectime)
logtarget = os.path.join(log_get_target)

# function to loop through files in the folder and sort them to lists depending on file extension
def lister():
    for file in files:
        filename = file.name.lower()
        if filename.endswith('_file_sort_log.txt'):
            continue
        if filename.endswith(('.xlsx', '.xls', '.csv')):
            sort_spreadsheets.append(file)
        elif filename.endswith(('.txt', '.docx', '.pdf')):
            sort_textfiles.append(file)
        elif filename.endswith(('.zip', '.rar', '.tar', '.7z')):
            sort_archives.append(file)
        elif filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            sort_images.append(file)
        elif filename.endswith(('.mp4', '.avi', '.mov', '.mkv')):
            sort_videos.append(file)
        elif filename.endswith(('.mp3', '.wav', '.ogg')):
            sort_audio.append(file)
        elif filename.endswith(('.pptx', '.ppt')):
            sort_presentations.append(file)
        elif filename.endswith(('.exe', '.msi')):
            sort_executables.append(file)
        else:
            sort_undetermined.append(file)

# ignore lists if there are no items to be displayed within
def checkfiles():
    for name, elems in meta.items():
        if len(elems)>0:
            print(f"{len(elems)} {name.lower()} detected in the directory being reviewed.")
            print("\n")
        else:
            pass

# details a for loop for better readibility of each file, contained in the identified type list
def checkfiles_details():
    for name, elems in meta.items():
        if len(elems)>0:
            print(f"\n{name} ({len(elems)} files) :")
            for item in elems:
                print("- ",item.name)
        else:
            pass
    vlb()

# match case for input on actions to take on files
def get_agreement():
    print("\nDo you want to move the files into their respective folders? (y/n)\n")
    match input().lower():
        case "y":
            createrelativedirs()
            mass_mover()
        case "n":
            print("\nOperation cancelled.")
        case "":
            print("\nOperation cancelled.")
        case _:
            print("Invalid input. Please enter 'y' or 'n'.")
            get_agreement()

# moves all files detected to the respective folders
def mass_mover():
    for folder_name, files in meta.items():
        destination = os.path.join(target, folder_name)

        os.makedirs(destination, exist_ok=True)
        for file in files:
            try:
                e = shutil.move(file, destination)
                success_log.append(e)
            except PermissionError:
                print(f"Permission denied: Unable to move {file} to {destination}.")
            except FileNotFoundError:
                print(f"File not found: {file}")
            except Exception as e:
                print(f"Error moving {file} to {destination}: {e}")

# logs operations in a .txt file in the same operation folder, .txt is timestamped to avoid overwriting itself
def log_events():
    if not success_log and not error_log and not lost_log:
        return
    with open(logtarget, "a") as log:
        log.write("Tracking log for sorting and moving operations held on ")
        log.write(str(exectime))
        log.write("\n")

        if len(success_log)>0:
            log.write(f"Successful operations ({len(success_log)}) :\n")
            for a in success_log:
                log.write(a + "\n")
        else:
            pass

        if len(error_log)>0:
            log.write(f"Errors in operations - please check those files are not currently open ({len(error_log)}) :\n")
            for b in error_log:
                log.write(b + "\n")
        else:
            pass

        if len(lost_log)>0:
            log.write(f"Files not found during the operation ({len(lost_log)}) :\n")
            for c in lost_log:
                log.write(c + "\n")
        else:
            pass
