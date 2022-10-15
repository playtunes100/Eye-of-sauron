import sys
import os
import getopt
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:

    def __init__(self, directory, handler=FileSystemEventHandler()):
        self.observer = Observer()
        self.handler = handler
        self.directory = directory

    def run(self):
        self.observer.schedule(
            self.handler, self.directory, recursive=False)
        self.observer.start()
        print("\nWatcher Running in {}/\n".format(self.directory))
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
        self.observer.join()
        print("\nWatcher Terminated\n")



class MyHandler(FileSystemEventHandler):

    def on_any_event(self, event):
        print(event) 
        if event.event_type == 'created':
            if not event.is_directory:
                
                extension = Tools.find_extension(event.src_path)
                print("---File Type: "+ extension)
                #-----------------------------------------------
                Tools.organise(event.src_path, extension)


class Tools():
    #Finds the file extension/suffix of a file
    def find_extension(path):
        for index, item in enumerate(reversed(path)):
            if item == '.':
                suffix = path[len(path)-index:len(path)]
                return suffix.lower()

    #takes new file's path and its type and moves it to corresponding folder
    def organise(src_path, type):
        folder_dict = {'Music':["aac","flac","m4a","mp3","ogg","wav","opus","mpga","weba","wma"],
                        'Images':["jpg","jpeg","png","gif","webp","ico","tif","bmp","xcf","svg"],
                        'Videos':["mp4","3gp","m4v","mkv","webm","mov","avi","wmv","mpg","flv"],
                        'Archives':["zip","rar","tar","7z","gz","xz","lzo","iso"],
                        'Documents':["pdf","epub","txt","docx","doc","xls","xlsx","ppt","pptx","odt","csv"],
                        'Applications':["exe","msi","dll","jar","apk","com","bat","bin","cmd"],
                        'Scripts':["py","js","htm","html","css","java","c","cpp","json","xml"]
                        }
               
        for folder in folder_dict:
            if type in folder_dict[folder]:
                head, path = os.path.split(src_path)
                target_path = head +"\\"+folder + "\\" + path
                print("Moving: "+src_path+" To: "+target_path)
                os.renames(src_path,target_path)
                print("Done")
            else:
                return type
     
    #used to organize files in the folder before running the Watcher           
    def organiser(path):
        unrecognized = []
        with os.scandir(path) as it:
            for entry in it:
                if not entry.name.startswith('.') and entry.is_file() and entry.name != 'eye.py':
                    extension = Tools.find_extension(entry.path)
                    unrecognized.append(Tools.organise(entry.path,extension))
            print("List of unrecognized filetypes:")
            print(set(unrecognized))
        
        
if __name__=="__main__":

    try:
        arguments, values = getopt.getopt(sys.argv[1:], "ho:w:", ["Help", "Organize", "Watch"])
        for currentArgument, currentValue in arguments:
    
            if currentArgument in ("-h", "--Help"):
                print("Thanks for using The Eye of sauron!\n\n This script has three arguments: \n 1. -w <folderpath> to activate the watcher in that folder. \n 2. -o <folderpath> to organize the folder before activating watcher.\n 3. -h for help")
            
            elif currentArgument in ("-o", "--Organize"):
                print("Organizing in "+ currentValue)
                Tools.organiser(currentValue)

            elif currentArgument in ("-w", "--Watch"):
                print("Starting Watcher in " + currentValue)
                w = Watcher(currentValue, MyHandler())
                w.run()
                         
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))