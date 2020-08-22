from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os


g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)

with open("Chandler/resources/chandler.png", 'r') as file:
    file_drive = drive.CreateFile({'test10008000': os.path.basename(file.name)})
    file_drive.SetContentFile(file.read())
    file_drive.Upload()