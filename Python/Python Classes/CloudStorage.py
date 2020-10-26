import dropbox

# C:/Users/nandu/Desktop/Python/Python Classes/Functions_copy.py
# Functions_copy

class TransferData:
    def __init__(self, accessToken):
        self.aT = accessToken

    def uploadFile(self, file_from, file_to):
        db = dropbox.Dropbox(self.aT)
        with open(file_from, "rb") as f:
            db.files_upload(f.read(), file_to)

AToken = "sl.AkBQBIogRkoqEu9HdhxlQijShFMGa587mwz2Z4HsnLmDYB0QM5zSyzSxFY5-N1_kOMfTX_H21MeIV-HVnLekDXdCsFVBrkTYZgfCHP3yzFth0V4TGmXmUEs6XRS5jLImCW3PKEB0aug"

cloudStoring = TransferData(AToken)

fileFrom = input("Please Give the File Path To Transfer ")
fileTo = input("Please Give the second File Path To Transfer ")

cloudStoring.uploadFile(fileFrom, fileTo)

print("Files Have Been Stored On Dropbox ;)")
