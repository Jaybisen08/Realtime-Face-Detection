import cv2
import cv2.data

modelPath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
model = cv2.CascadeClassifier(modelPath)

camera = cv2.VideoCapture(0)

# Create resizable window
cv2.namedWindow("faces", cv2.WINDOW_NORMAL)

# Make fullscreen
cv2.setWindowProperty(
    "faces",
    cv2.WND_PROP_FULLSCREEN,
    cv2.WINDOW_FULLSCREEN
)

while True:
    status, image = camera.read()

    faces = model.detectMultiScale(image, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 3)

        cv2.putText(
            image,
            "Face detected",
            (x, y - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 10),
            2
        )

    cv2.imshow("faces", image)

    # Press 'a' to exit
    if cv2.waitKey(1) == ord('a'):
        break

camera.release()
cv2.destroyAllWindows()
