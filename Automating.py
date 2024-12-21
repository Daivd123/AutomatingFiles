# OS MODULE
# import os imports all OS methods
# print(dir(os)) ofr system related methods
# os.getcwd() for directory path
# os.mkdir("") for creating a new folder (add name in brackets)
# os.listdir() shows files in current path
# os.path.exists("C121") will show if file is there or not
# root,ext=os.path.splitext("tree.png")  Splits text into two variables (root, ext)
# OR os.path.splitext("tree.png") 

#SHUTIL MODULE
#Offers a number high level operations on files and collection files.
#shutil.copy(source,destination)
#shutil.move(source,destination)
#shutil.copy("Documents/tree.png)",Desktop)

#Automating the file Seggregation --> Separating file automatically w/ Program
import sys
import time
import random

import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/David/Downloads"
to_dir = "C:/Users/David/Downloads/Downloaded_Files"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2','.mp3', ".mp4", '.mpeg', '.mpe', '.mpv','.m4v', ".m4v", '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx', '.csv', '.pdf', '.txt'],
    'Setup_Files': ['.exe', '.bin', 'cmd', 'msi','.dmg']
}

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        name, extension = os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                file_name = os.path.basename(event.src_path)
                print("Downloaded" + file_name)
                path1 = from_dir + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + "/" + key + '/' + file_name

            if os.path.exists(path2):
                print("directory exists")
                print("Moving" + file_name + ".........")
                shutil.move(path1,path3)

                time.sleep(1)

            else:
                print("Making Directory...")
                os.makedirs(path2)
                print("Moving" + file_name + ".........")
                shutil.move(path1,path3)
                time.sleep(1)

event_handler = FileMovementHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive = True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("Stopped!")
    observer.stop()

