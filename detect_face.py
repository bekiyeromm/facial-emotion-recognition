import cv2
import glob
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
path = "surprise/*.*"
image_number = 1
image_list = glob.glob(path)

# extract images
for file in image_list[0:9]:
    print(file)
    img = cv2.imread(file,1)
    #convet the image to gray scale 
    #because harcascade works on gray scale image
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray,1.3,5)
    try:
        for (x,y,w,h) in face:
            rio_color = img[y:y+h, x:x+w]
        resized = cv2.resize(rio_color,(128,128))
        cv2.imwrite("extractedface/surprise/"+'surprise'+str(image_number)+".png",resized)
    except:
        print("no face detected")  
    image_number = image_number + 1