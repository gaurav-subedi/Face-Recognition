import cv2

# Load the Haar cascade for face detection
haar_face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')

# Open the default camera (usually the webcam)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open video device")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # If frame reading was not successful, break the loop
    if not ret:
        print("Failed to grab frame")
        break

    # Convert the frame to grayscale as face detection requires grayscale images
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = haar_face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    # Draw a green rectangle around each detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Display the resulting frame with detected faces
    cv2.imshow("Face Detection", frame)
    
    # Wait for 1 ms for a key press and get the key code.
    # If 'q' or 'Esc' is pressed, break the loop.
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:  # 27 is the Esc key
        print("Exiting...")
        break

# When everything is done, release the capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
