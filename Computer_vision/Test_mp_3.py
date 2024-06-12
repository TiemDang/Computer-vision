import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Khởi tạo Hands detector
with mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Cannot read video frame.")
            break

        # Chuyển đổi ảnh sang không gian màu RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Phát hiện bàn tay trong ảnh
        results = hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Đếm số ngón tay
                num_fingers = 0
                # Vị trí các điểm đặc trưng của bàn tay
                finger_tips = [hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP],
                               hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP],
                               hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP],
                               hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP],
                               hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]]
                # Đếm số ngón tay dựa trên vị trí của các điểm đặc trưng
                for i in range(1, 5):
                    if finger_tips[i].y < finger_tips[i - 1].y:
                        num_fingers += 1
                # Vẽ các điểm đặc trưng và số ngón tay lên ảnh
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                cv2.putText(image, f'Number of fingers: {num_fingers}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 255, 0), 2)

        cv2.imshow('Hand Counting', image)

        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
