import os
import shutil

sourcePath = input("Enter the Path of the directory ")

listOfItems = os.listdir(sourcePath)

for i in listOfItems:
    FileName, Extension = os.path.splitext(i)
    print(Extension)
    print(FileName)
    if(Extension == ''):
        continue

    finalPath = sourcePath + '/' + Extension
    exist = os.path.exists(finalPath)
    if(exist == False):
        os.mkdir(finalPath)
    shutil.move(sourcePath+'/'+i, finalPath+'/'+i)
