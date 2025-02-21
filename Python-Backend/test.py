import cv2

cap = cv2.VideoCapture(0)  # Try 1, 2, 3 if needed

if not cap.isOpened():
    print("❌ Error: Could not open video device")
    exit()
else:
    print("✅ Camera Opened Successfully!")

while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Failed to grab frame")
        break

    cv2.imshow("Face Detection Debug", frame)  # Show live video

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        print("🔴 Exiting...")
        break

cap.release()
cv2.destroyAllWindows()
