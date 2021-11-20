import cv2
import random
import dropbox
import time

startTime = time.time()

def takeSnap():
    randomNumber = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        imageName = 'Unknownpic' + str(randomNumber) + '.jpeg'
        cv2.imwrite(imageName,frame)
        startTime = time.time
        result = False
    
    return imageName
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFile(imageName):
    myAT = 'qzzH1jgmancAAAAAAAAAARyBSmhTt1yyrBcrh9tVYovIby_0GP6GJH0MWv93NGjy'
    fileFrom = imageName
    fileTo = '/Snaps/' + imageName
    dbx = dropbox.Dropbox(myAT)

    with open(fileFrom,'rb') as source:
        dbx.files_upload(source.read(),fileTo,mode = dropbox.files.WriteMode.overwrite)


def main():
    while(True):
        if((time.time()-startTime>=2592000)):
            imageFileName = takeSnap()
            uploadFile(imageFileName)

main()