Real-Time Face Detector using OpenCV and Haar Cascade

This project is a real-time face detection system built with Python, OpenCV, and the Haar Cascade algorithm.
It detects faces from a webcam or a video file by simply changing one argument in the code.

Overview

The Haar Cascade algorithm is a machine learning-based object detection method used to identify objects in images or videos.
In this project, it is used to detect human faces in real time.

Features

Real-time face detection using webcam or video file

Fast and efficient performance

Works with multiple faces in a single frame

Lightweight and easy to set up

How It Works

Opens the webcam or loads a video file

Converts each frame to grayscale for faster processing

Uses a pre-trained Haar Cascade Classifier to detect faces

Draws rectangles around detected faces

Displays the video output with detections in real time

Technologies Used

Python 3

OpenCV (cv2 library)

Haar Cascade Classifier (haarcascade_frontalface_default.xml)

Installation and Usage
# 1. Clone this repository
git clone https://github.com/YourUsername/face-detector.git

# 2. Navigate to the project directory
cd face-detector

# 3. Install dependencies
pip install opencv-python

# 4. Run the script for webcam detection
python face_detector.py

Using a Video File Instead of Webcam

In your code, you will see this line:

webcam = cv2.VideoCapture(0)   # 0 for default webcam


To detect faces in a video file, replace it with:

webcam = cv2.VideoCapture('video.mp4')   # path to your video file

Output

Detects faces in real time from webcam or video input

Draws bounding boxes around detected faces

Future Enhancements

Add eye or smile detection

Integrate emotion recognition

Develop a face-based attendance or security system
