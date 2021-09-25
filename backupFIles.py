import os 
import shutil
source = input ("Enter the folder name.:")
destination = input ("Type in destination folder")
source = source+'/'
destination = destination+'/'
list_files = os.listdir(source)
for file in list_files: 
    shutil .copy((source+ file), destination )