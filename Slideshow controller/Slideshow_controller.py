import cv2
import mediapipe as mp
import pyautogui
import time

# -------------------- INITIALIZATION --------------------
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

last_action_time = 0
cooldown = 1.2
status_text = "Waiting for hand..."

# -------------------- FINGER LOGIC --------------------
def fingers_up(hand_landmarks):
    fingers = []

    # Thumb (simple logic)
    if hand_landmarks.landmark[4].x > hand_landmarks.landmark[2].x:
        fingers.append(1)
    else:
        fingers.append(0)

    tips = [8, 12, 16, 20]
    pips = [6, 10, 14, 18]

    for tip, pip in zip(tips, pips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers

# -------------------- MAIN LOOP --------------------
while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    status_text = "No hand detected"

    if result.multi_hand_landmarks and result.multi_handedness:
        for idx, hand_landmarks in enumerate(result.multi_hand_landmarks):

            # Dominant hand check (Right hand only)
            hand_label = result.multi_handedness[idx].classification[0].label
            if hand_label != "Right":
                continue

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            fingers = fingers_up(hand_landmarks)
            current_time = time.time()

            # -------------------- GESTURE ACTIONS --------------------
            if fingers == [0, 1, 0, 0, 0]:
                status_text = "NEXT SLIDE"
                if current_time - last_action_time > cooldown:
                    pyautogui.press("right")
                    last_action_time = current_time

            elif fingers == [0, 0, 0, 0, 0]:
                status_text = "PREVIOUS SLIDE"
                if current_time - last_action_time > cooldown:
                    pyautogui.press("left")
                    last_action_time = current_time

            elif fingers == [1, 1, 1, 1, 1]:
                status_text = "PAUSE / PLAY"
                if current_time - last_action_time > cooldown:
                    pyautogui.press("space")
                    last_action_time = current_time

            else:
                status_text = "Gesture not recognized"

            break  # Only one dominant hand

    # -------------------- UI OVERLAY --------------------
    cv2.putText(
        frame,
        status_text,
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Day 5 - Gesture Controlled Presentation", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

#Parth-i s-cutie
