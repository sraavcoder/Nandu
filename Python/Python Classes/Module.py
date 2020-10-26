import os
import shutil

# os.mkdir("I Created A Folder")

# path = os.getcwd()

path = "C:/Users/Teju Sraav/Desktop/WhitehatJr Python/Python Basics/Module.py"
# exist = os.path.exists(path)
FileName, Extension = os.path.splitext(path)
print(Extension)

# path = "C:/Users/Teju Sraav/Desktop/WhitehatJr Python/Python Basics"
# print(os.listdir(path))

# path = "C:/Users/Teju Sraav/Desktop/WhitehatJr Python/Python Basics"
# print("Before Copiying The Files")
# print(os.listdir(path))

# sourcePath = "C:/Users/Teju Sraav/Desktop/WhitehatJr Python/Python Basics/Test.txt"
# destinationPath = "C:/Users/Teju Sraav/Desktop/WhitehatJr Python/TEXT.py"

# variable = shutil.move(sourcePath, destinationPath)
