import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

def recognize_gesture(hand_landmarks):
    """Recognizes simple hand gestures (Open Hand or Fist)."""
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    index_pip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]
    if index_tip.y < index_pip.y:  # Index finger raised
        return "Open Hand ✋"
    else:
        return "Fist 👊"

def detect_hands(frame):
    """Detects hands, recognizes gestures, and draws landmarks.
    Returns a tuple: (processed_frame, gesture_text)
    """
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)
    gesture_text = "No Hand"

    if result.multi_hand_landmarks:
        # If more than one hand is detected, this will update gesture_text for each hand.
        # You can modify this behavior if you want to handle multiple gestures differently.
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture_text = recognize_gesture(hand_landmarks)
    cv2.putText(frame, f"Gesture: {gesture_text}", (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
    return frame, gesture_text
