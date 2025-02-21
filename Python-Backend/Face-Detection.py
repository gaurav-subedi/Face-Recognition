import cv2
import asyncio
import websockets
import json
import threading
import os
from hand_tracking import detect_hands

# Global set to hold connected WebSocket clients
clients = set()
ws_loop = None  # Will store the WebSocket server's event loop

# --- Load Haar Cascade for Face Detection ---
haar_path = os.path.join(os.getcwd(), 'data', 'haarcascade_frontalface_alt.xml')
haar_face_cascade = cv2.CascadeClassifier(haar_path)
if haar_face_cascade.empty():
    print("Error: Haarcascade file not found or not loaded correctly:", haar_path)
    exit()
else:
    print("Haarcascade Loaded Successfully!")

# --- Open the Camera ---
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open video device")
    exit()
else:
    print("Camera Opened Successfully!")

# --- WebSocket Server Functions ---
# Make the 'path' parameter optional so it works with different websockets versions.
async def ws_handler(websocket, path=None):
    print("New client connected")
    clients.add(websocket)
    try:
        await websocket.wait_closed()
    except Exception as e:
        print("WebSocket handler error: " + str(e))
    finally:
        clients.remove(websocket)
        print("Client disconnected")

async def start_server():
    server = await websockets.serve(ws_handler, "localhost", 8765)
    print("WebSocket Server Started on ws://localhost:8765")
    return server

def start_ws_server():
    global ws_loop
    ws_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(ws_loop)
    ws_server = ws_loop.run_until_complete(start_server())
    try:
        ws_loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        ws_server.close()
        ws_loop.run_until_complete(ws_server.wait_closed())
        ws_loop.close()

# Start the WebSocket server thread (daemon=True ensures it exits when main thread ends)
ws_thread = threading.Thread(target=start_ws_server, daemon=True)
ws_thread.start()

# --- Main Camera Capture and Processing Loop ---
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Convert to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = haar_face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.05,  # Adjusted parameter for sensitivity
        minNeighbors=3     # Adjusted parameter for sensitivity
    )
    num_faces = len(faces)

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Process hand detection and overlay gesture information.
    frame, gesture_text = detect_hands(frame)

    # Debug print to check detections
    print("Detected faces: " + str(num_faces) + " | Gesture: " + gesture_text)

    # Create JSON detection data
    detection_data = {
        "faces_detected": num_faces,
        "gesture": gesture_text
    }

    # Send detection data to connected WebSocket clients (if any)
    if clients and ws_loop:
        async def send_data():
            data = json.dumps(detection_data)
            for ws in clients.copy():
                try:
                    await ws.send(data)
                except Exception as e:
                    print("Error sending data: " + str(e))
        asyncio.run_coroutine_threadsafe(send_data(), ws_loop)

    # Display the processed frame
    cv2.imshow("Face & Hand Detection with Gestures", frame)

    # Exit on 'q' or 'ESC'
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        print("Exiting...")
        break

# Clean up resources
cap.release()
cv2.destroyAllWindows()
