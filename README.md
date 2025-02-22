# Face & Gesture Detection System

## Overview
This project is a real-time Face & Gesture Detection System that detects faces and hand gestures using Python (OpenCV, MediaPipe) and sends the detection results to a C# UI via WebSockets. The C# UI then updates the displayed face count and recognized gesture in real-time.

## Features
- Real-time Face Detection using OpenCV Haar Cascade  
- Hand Gesture Recognition using MediaPipe  
- WebSocket Communication between Python and C#  
- Live UI Update displaying detected faces and gestures  
- Multi-threaded WebSocket Server for seamless data streaming  

## Technologies Used
### Python (Backend)
- OpenCV (Face Detection)
- MediaPipe (Hand Tracking & Gesture Recognition)
- WebSockets (Communication with C# UI)
- AsyncIO & Threading (WebSocket Server)

### C# (Frontend - UI)
- WinForms (User Interface)
- WebSockets (Receiving data from Python)
- Multi-threaded Event Handling (UI updates)

## Installation & Setup
### Step 1: Clone the Repository
```bash
git clone https://github.com/gaurav-subedi/face-gesture-detection.git
cd face-gesture-detection
```

### Step 2: Install Python Dependencies
Make sure you have Python 3.8+ installed, then run:
```bash
pip install -r requirements.txt
```

### Step 3: Set Up C# Project
1. Open the C# solution in Visual Studio.
2. Ensure Newtonsoft.Json is installed via NuGet.
3. Compile and run the C# UI (FaceHandDetectionUI).

### Step 4: Run the Python WebSocket Server
```bash
python Face-Detection.py
```
If the server starts successfully, you should see:
```
WebSocket Server Started on ws://localhost:8765
```

### Step 5: Run the C# UI
- Launch the FaceHandDetectionUI.exe (or run from Visual Studio).
- The UI should now receive real-time updates from Python.

## Usage
- Make sure your camera is connected before running.
- The C# UI will update the number of detected faces and the recognized hand gesture.
- Press `1 and Q` or `ESC` in the Python window to exit.

## Future Improvements
1. Upgrade Face Detection to Deep Learning (DNN-based models)  
2. Add support for more hand gestures (Thumbs Up, Victory Sign, etc.)  
3. Integrate with a VR/AR system for gesture-based interactions  

## Contributing
Feel free to submit issues, fork the repo, and make pull requests!


