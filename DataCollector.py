import cv2
video =cv2.VideoCapture(0)
facedetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    sucess, vid = video.read()
    face=facedetect.detectMultiScale(vid,1.5,5)

    for x,y,w,z in face:
        cv2.rectangle(vid, (x, y), (x + w, +z), (0, 255, 0), 3)
        cv2.imshow("vid", vid)

    k =  cv2.waitKey(1)
    if k == ord("a"):
        break








