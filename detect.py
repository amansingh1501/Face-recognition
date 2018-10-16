
import cv2                  # Importing the opencv
import NameFind

# import the Haar cascades for face and eye ditection

face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml')
recognise = cv2.face.HaarCascade_create()
cap = cv2.VideoCapture(0)
ID = 0

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                    # Convert the Camera to gray
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  
    # ---------------------------------- FACE DETECTION ------------------------------------

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)             # Detect the faces and store the positions
    for (x, y, w, h) in faces:                                      # Frames  LOCATION X, Y  WIDTH, HEIGHT
        gray_face = cv2.resize((gray[y: y+h, x: x+w]), (110, 110))  # The Face is isolated and cropped
        eyes = eye_cascade.detectMultiScale(gray_face)
        for (ex, ey, ew, eh) in eyes:
            NameFind.draw_box(gray, x, y, w, h)
            NAME = NameFind.ID2Name(ID, conf)
            NameFind.DispID(x, y, w, h, NAME, gray)

    cv2.imshow('Face Detection Using Haar-Cascades ', gray)         # Show the video
    if cv2.waitKey(1) & 0xFF == ord('q'):                           # Quit if the key is Q
        break
cap.release()
cv2.destroyAllWindows()
