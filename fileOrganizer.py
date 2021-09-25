from genericpath import exists
import os
import shutil
path = input("Enter the Name of Directory that will be sorted:")
list_files = os.listdir(path)
for file in list_files: 
    name,ext = os.path.splitext(file)
    ext = ext[1:]
    if ext == '':
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file, path+ '/'+ext+ '/'+file)
    else: 
        os.makedirs (path+ '/'+ ext)
        shutil.move(path+'/'+file, path+ '/'+ext+ '/'+file)