# 🎭 Real-Time Face Detection using OpenCV

<div align="center">

✨ *A real-time AI face detection project using Python & OpenCV* ✨

</div>

---

# 📌 Description

This project is a **Real-Time Face Detection System** built using **Python** and **OpenCV**.  
It uses the **Haar Cascade Classifier** to detect human faces through a webcam in real time.

The application captures live video from the camera, detects faces instantly, and draws rectangles around detected faces along with a detection label.

---

# 🚀 Features

✅ Real-time face detection  
✅ Webcam integration  
✅ Fullscreen camera mode  
✅ Face highlighting with rectangles  
✅ Live detection text display  
✅ Beginner-friendly OpenCV project  

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Programming Language |
| 👁️ OpenCV | Computer Vision |
| 🎥 Webcam | Live Video Capture |

---

# 📂 Project Structure

```bash
📦 Face-Detection-Project
 ┣ 📜 face_detection.py
 ┣ 📜 requirements.txt
 ┗ 📜 README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

Create a `requirements.txt` file and add:

```txt
opencv-python
```

---

# ▶️ Run the Project

```bash
python face_detection.py
```

---

# 💻 Source Code

```python
import cv2
import cv2.data

modelPath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
model = cv2.CascadeClassifier(modelPath)

camera = cv2.VideoCapture(0)

cv2.namedWindow("faces", cv2.WINDOW_NORMAL)

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

    if cv2.waitKey(1) == ord('a'):
        break

camera.release()
cv2.destroyAllWindows()
```

---

# 🎮 Controls

| Key | Action |
|-----|--------|
| `A` | Exit Application |

---

# 🌟 Future Improvements

🔹 Eye detection  
🔹 Smile detection  
🔹 Face recognition system  
🔹 AI attendance system  
🔹 Face blur feature  
🔹 Screenshot capture  

---

# 📸 Output Preview

📷 Live webcam feed with real-time face detection.

---

# 👨‍💻 Author

## Jay Bisen

💡 Passionate about AI, ML & Computer Vision

---

# 📄 License

📝 This project is open-source and available under the **MIT License**.

---

<div align="center">

⭐ If you like this project, don't forget to star the repository ⭐

</div>
