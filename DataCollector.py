import cv2
video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
count=0
while True:
    sucess, vid = video.read()
    face = facedetect.detectMultiScale(vid, 1.8, 5)

    for x, y, w, h in face:
        count+=1
        name ='./images/mask/' + str(count) +".jpg"
        print ('creating images.............'+ name)
        cv2.imwrite(name,vid[y:y+h,x:x+w])
        cv2.rectangle(vid, (x, y), (x + w, y+h), (0, 255, 0), 3)
    cv2.imshow("vid", vid)
    k = cv2.waitKey(1)
    if count == 5000:
        break






