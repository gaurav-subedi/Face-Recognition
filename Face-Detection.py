import cv2
from hand_tracking import detect_hands  # Import hand tracking module

# Load Haar cascade for face detection
haar_face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')

# Open the default camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video device")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Convert to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = haar_face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Apply hand tracking on the frame
    frame = detect_hands(frame)

    # Show the frame with both face and hand detection
    cv2.imshow("Face & Hand Detection", frame)

    # Exit when 'q' or Esc is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        print("Exiting...")
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
