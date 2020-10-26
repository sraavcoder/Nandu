import os
import shutil
# C:/Users/Teju Sraav/Desktop/WhitehatJr Python/All
# C:/Users/Teju Sraav/Desktop/Backup

sourcePath = input("Enter the Path of the directory ")
backupPath = input("Enter the Path of the Backup Directory ")

listOfItems = os.listdir(sourcePath)
print(listOfItems)

for i in listOfItems:
    FileName, Extension = os.path.splitext(i)
    if(Extension == ''):
        break

    path = sourcePath+'/'+i
    shutil.copy(path, backupPath+'/')
