from os import access
import dropbox

class TransferData :
    def __init__(self, access_token) :
        self.access_token = access_token

    def upload_file(self, file_from, file_to) :
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb') 
        dbx.files_upload(f.read(), file_to)

def main() :
    access_token = 'sl.A0tFUR8kaW5NFkVXq08zooETthsLe0OyAtCY3AhI0QELSiXN6ZNwmArwlk2yCubM9LP3J6Q--4h6J8kWiQdvGCHvGAFi-vFupqf-Zs3H3AT7gwbL3Ta0aljbzg2Jwckv7zLltkY'
    transferData = TransferData(access_token)
    file_from = input("Enter the file path: ")
    file_to = input("Enter the full path")

    transferData.upload_file(file_from, file_to)
    print("File has been moved")

main()