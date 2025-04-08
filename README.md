# Virtual Cam Python 🎥

## Description
Virtual Cam Python is a versatile tool designed to stream video frames from various sources (files, webcams) through a virtual camera. This project is perfect for developers looking to integrate live or recorded video into their applications without the need for physical hardware.

## Features
- **Video Streaming**: Captures video frames from files and streams them through a virtual camera.
- **Real-Time Processing**: Supports real-time video processing using OpenCV.
- **User Control**: Pauses streaming on user input ('q' to quit).
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux.

## Installation
To get started with Virtual Cam Python, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/gag3301v/Virtual-Cam-Python.git
   cd Virtual-Cam-Python
   ```

2. Install dependencies using pip:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Here’s how you can use the program:

### Streaming Video from a File
```python
# main.py
import cv2
from pyvirtualcam import Camera

def stream_video(file_path):
    cap = cv2.VideoCapture(file_path)
    cam = Camera(width=640, height=480, fps=30)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        with cam:
            cam.send(frame)
            cam.sleep_until_next_frame()

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    cam.stop()

if __name__ == "__main__":
    file_path = "path_to_your_video_file.mp4"
    stream_video(file_path)
```

### Streaming Video from a Webcam
```python
# main.py
import cv2
from pyvirtualcam import Camera

def stream_webcam():
    cap = cv2.VideoCapture(0)
    cam = Camera(width=640, height=480, fps=30)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        with cam:
            cam.send(frame)
            cam.sleep_until_next_frame()

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    cam.stop()

if __name__ == "__main__":
    stream_webcam()
```

## Configuration
- **Camera Resolution**: Adjust `width` and `height` in the `Camera` constructor.
- **Frame Rate**: Set the `fps` parameter in the `Camera` constructor.

## Tests
No automated tests are provided at this time. However, you can manually test the script by running it and ensuring that the video streams correctly through the virtual camera.

## Project Structure
```
Virtual-Cam-Python/
├── main.py
└── requirements.txt
```

## Contributing
We welcome contributions from the community! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to explore and contribute to Virtual Cam Python! 🌟