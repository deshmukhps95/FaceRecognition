import os
import cv2
import numpy as np
from PIL import Image

global os,np,PIL,cv2
recognizer = cv2.createLBPHFaceRecognizer();
path = 'dataSet'

def getImageWithID(path):
    
    faces=[];
    IDs = [];
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L');
        faceNp=np.array(faceImg,'uint8');
        
        ID =int(os.path.split(imagePath)[-1].split('.')[1]);     

        #print ID

        faces.append(faceNp);
        
        IDs.append(ID);
        
        #cv2.imshow("training",faceNp)

        cv2.waitKey(10)
        
    return IDs,faces	
Ids,faces = getImageWithID(path)

recognizer.train(faces,np.array(Ids))

recognizer.save('Recognizer/trainingData.yml')
cv2.destroyAllWindows()
execfile("detector.py")
