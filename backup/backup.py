import os
import shutil
source=input("source folder:")
destination=input("destination folder:")
source=source+'/'
destination=destination+'/'
listOfFiles=os.listdir(source)
for file in listOfFiles:
    shutil.copy((source+file),destination)
