__author__ = "David Amador"
__twitter__ = "@DJ_Link"
__description__ = "Script to find all Visual Studio *.vs folders within a directory, can optionally can be deleted, will send to recicle bin if possible"
__url__ = 'https://github.com/DJLink/visualstudio_VS_folder_cleaner'

import os, sys, send2trash

FOLDER_SEARCH = ".vs"

class bcolors:
    OK = '\033[92m'
    WARNING = '\033[91m'

def calculate_folder_size(folder):
    folder_size = 0
    for (path, dirs, files) in os.walk(folder):
        for file in files:
            folder_size += os.path.getsize(os.path.join(path, file))
    
    return folder_size

#author:whereisalext https://stackoverflow.com/a/31631711
def human_bytes(bytes):
   bytes = float(bytes)
   KB = float(1024)
   MB = float(KB ** 2) # 1,048,576
   GB = float(KB ** 3) # 1,073,741,824
   TB = float(KB ** 4) # 1,099,511,627,776

   if bytes < KB:
      return '{0} {1}'.format(bytes,'Bytes' if 0 == bytes > 1 else 'Byte')
   elif KB <= bytes < MB:
      return '{0:.2f} KB'.format(bytes/KB)
   elif MB <= bytes < GB:
      return '{0:.2f} MB'.format(bytes/MB)
   elif GB <= bytes < TB:
      return '{0:.2f} GB'.format(bytes/GB)
   elif TB <= bytes:
      return '{0:.2f} TB'.format(bytes/TB)

def query_yes_no(question, default="no"):
    valid = {"yes": True, "y": True, "no": False, "n": False}

    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'y' or 'n' \n")

# MAIN

if len(sys.argv)<=1:
    print("Usage:", sys.argv[0], "<root folder to search>")
    sys.exit()
	
ask_each_folder = False;

ROOT_SEARCH = sys.argv[1]

if len(sys.argv)>=2:
	if sys.argv[1] == '-i':
		ask_each_folder = True;
		ROOT_SEARCH = sys.argv[2]

all_folders = list()

all_folders_size = 0

deleted_amount = 0

# Find all folders
for root, dirs, files in os.walk(ROOT_SEARCH):
    for dir in dirs:
        if dir.endswith(FOLDER_SEARCH):
            folder = os.path.join(root, dir)
            size = calculate_folder_size(folder)
            print(bcolors.OK + folder, "(", human_bytes(size), ")")

            if  ask_each_folder ==  True:
                if  query_yes_no(bcolors.WARNING + "Delete?", "no")   ==  True:
                    send2trash.send2trash(folder)
                    deleted_amount+=size
            else:
                all_folders.append(folder)
            
            all_folders_size += size


#Query user for deletion (sends to recicle bin if possible)
if len(all_folders) > 0 :
    print(bcolors.OK + "Full Size:", human_bytes(all_folders_size))
    if query_yes_no(bcolors.WARNING + "Do you wish to delete all?", "no") == True:
        print("Deleting...")
			
        for dir in  all_folders:
            send2trash.send2trash(dir)

    print("Done!")
elif ask_each_folder ==  False:
    print(bcolors.OK + "No folders found")

if  ask_each_folder ==  True:
    print(bcolors.OK + "Found :", human_bytes(all_folders_size))
    print(bcolors.OK + "Cleaned :", human_bytes(deleted_amount))
