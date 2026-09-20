from sorter import *
from mover import *

def interface():
    print("Welcome to the lazy sorter ! \n\nUse it to sort and filter all clutered items in a folder into subfolders based on the type of file (i.e. images, documents or videos)")
    print("To use this program, drop its folder in the destination you want to sort out.")
    print("\nThe lazy sorter will be executed on all files -not folders- in",target)
    print("\nPlease pick an option :")

interface()
print("\n")
lister()
checkfiles()
checkfiles_details()
get_agreement()
log_events()
input("Press Enter to exit...")