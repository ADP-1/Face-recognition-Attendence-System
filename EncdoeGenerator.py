import cv2
import face_recognition
import pickle
import os

# importing studnet image
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath , path)))
    print(path)
    print(os.path.splitext(path))
print(len(imgList))
