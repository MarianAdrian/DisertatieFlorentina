"""
input: a loaded image; 
output: [[x,y],[width,height]] of the detected mouth area
"""

import cv2

def findmouth(img):

  # INITIALIZE: loading the classifiers
  haarFace = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
  haarMouth = cv2.CascadeClassifier('haarcascade_mouth.xml')
  # running the classifiers
  #storage = cv2.CreateMemStorage()
  #storage = 0
  #detectedFace = cv2.HaarDetectObjects(img, haarFace, storage)
  #detectedMouth = cv2.HaarDetectObjects(img, haarMouth, storage)

  detectedFace = haarFace.detectMultiScale(
                 img,
                 scaleFactor=1.2, #increase if wrong faces are detected
                 minNeighbors=5,
                 minSize=(30, 30),
                )
  detectedMouth = haarMouth.detectMultiScale(
                  img, 
                  scaleFactor=1.2, #increase if wrong faces are detected
                  minNeighbors=5,
                  minSize=(30, 30),
                )
  # FACE: find the largest detected face as detected face
  maxFaceSize = 0
  maxFaceIdx = 0
  index = 0
  for (x, y, w, h) in detectedFace:    #detect the largest face
    if w*h > maxFaceSize:
      maxFaceSize = w*h
      maxFaceIdx = index
    index = index+1
  maxFace = detectedFace[maxFaceIdx]

  if len(maxFace): # did not detect face
    return 2

  def mouth_in_lower_face(mouth,face):
    # if the mouth is in the lower 2/5 of the face 
    # and the lower edge of mouth is above that of the face
    # and the horizontal center of the mouth is the center of the face
    if (mouth[1] > face[1] + face[3] * 3 / float(5) 
      and mouth[1] + mouth[3] < face[1] + face[3]
      and abs((mouth[0] + mouth[2] / float(2)) 
        - (face[0] + face[2] / float(2))) < face[2] / float(10)):
      return True
    else:
      return False

  # FILTER MOUTH
  filteredMouth = []
  if detectedMouth:
   for mouth in detectedMouth:
    if mouth_in_lower_face(mouth,maxFace):
      filteredMouth.append(mouth) 
  
  maxMouthSize = 0
  for mouth in filteredMouth:
    if mouth[3]* mouth[2] > maxMouthSize:
      maxMouthSize = mouth[3]* mouth[2]
      maxMouth = mouth
  print(len(maxMouth))
  try:
    return maxMouth
  except UnboundLocalError:
    return 2

