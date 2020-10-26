import os

file1 = input("Enter The First File Location You Want To Swap ")
file2 = input("Enter The Second File Location You Want To Swap ")


def swapFileData(f1, f2):
    fl1 = open(f1, 'r')
    fl2 = open(f2, 'r')
    ln1 = fl1.readlines()
    ln2 = fl2.readlines()

    fl1.close()
    fl2.close()

    fl1 = open(f1, 'w')
    fl2 = open(f2, 'w')

    fl1.write('')
    fl2.write('')

    for i in ln1:
        fl2.write(i)
    for i in ln2:
        fl1.write(i)


exist1 = os.path.exists(file1)
exist2 = os.path.exists(file2)

if(exist1 == True and exist2 == True):
    swapFileData(file1, file2)
elif (exist1 == False or exist2 == False):
    print("Pls Give The Path Correctly")
