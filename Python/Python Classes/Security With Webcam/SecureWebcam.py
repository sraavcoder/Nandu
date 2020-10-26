import time
import random
import dropbox
import cv2

str_Time = time.time()

def Take_Snapshot():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        imageName = "Img"+str(number)+".png"
        cv2.imwrite(imageName, frame)
        str_Time = time.time()
        result = False

    return imageName

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadImage(imageName):
    AToken = "sl.AkBQBIogRkoqEu9HdhxlQijShFMGa587mwz2Z4HsnLmDYB0QM5zSyzSxFY5-N1_kOMfTX_H21MeIV-HVnLekDXdCsFVBrkTYZgfCHP3yzFth0V4TGmXmUEs6XRS5jLImCW3PKEB0aug"
    fileFrom = imageName
    fileTo = "/Test/"+(imageName)

    db = dropbox.Dropbox(AToken)
    with open(fileFrom, "rb") as f:
        db.files_upload(f.read(), fileTo, mode=dropbox.files.WriteMode.overwrite)
        print("Files Uploaded!!")

def main():
    while(True):
        if((time.time() - str_Time) >= 300):
            name = Take_Snapshot()
            uploadImage(name)

main()
