
import cv2
from ultralytics import YOLO

# Use 0 for Webcam, or "video.mp4" for a file
# cap = cv2.VideoCapture('w002_converted.avi') 
# cap = cv2.VideoCapture('w025_converted.avi') 
cap = cv2.VideoCapture('evaluation.mp4') 
model = YOLO(r"D:\resume-project\suspence-detection\weponse-train\yolov8n.pt")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
      
 # Run detection
    results = model(frame)

    # Draw results on frame
    annotated_frame = results[0].plot()

    # Show output
    cv2.imshow("Detection", annotated_frame)
  # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()










# import cv2
# from ultralytics import YOLO
# try:
#     import mediapipe as mp
#     # Check if solutions attribute exists (for compatibility)
#     if hasattr(mp, 'solutions'):
#         mediapipe_available = True
#     else:
#         raise AttributeError("MediaPipe solutions not available")
# except (ImportError, AttributeError):
#     print("MediaPipe not available or incompatible. Pose detection will be skipped.")
#     mediapipe_available = False
#     mp = None

# # Load models
# weapon_model = YOLO("suspence-detection/weponse-train/yolov8n.pt")   # your trained weapon model
# if mediapipe_available:
#     pose = mp.solutions.pose.Pose()
#     mp_draw = mp.solutions.drawing_utils
# else:
#     pose = None
#     mp_draw = None

# # Open camera
# cap = cv2.VideoCapture('n014_converted.avi')
# # cap = cv2.VideoCapture('w025_converted (1).avi') 


# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # ---------------- YOLO (Weapon Detection) ----------------
#     results = weapon_model(frame)
#     weapon_detected = False

#     for r in results:
#         for box in r.boxes:
#             cls = int(box.cls[0])
#             label = weapon_model.names[cls]

#             if label == "weapon":
#                 weapon_detected = True

#     # ---------------- MediaPipe (Behavior Detection) ----------------
#     aggressive_pose = False
#     if mediapipe_available and pose:
#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         result_pose = pose.process(rgb_frame)

#         if result_pose.pose_landmarks:
#             mp_draw.draw_landmarks(frame, result_pose.pose_landmarks,
#                                    mp.solutions.pose.POSE_CONNECTIONS)

#             # Simple behavior logic (example)
#             # If hands are too high → suspicious (fake rule)
#             landmarks = result_pose.pose_landmarks.landmark
#             if landmarks[15].y < 0.3:  # left wrist
#                 aggressive_pose = True

#     # ---------------- Decision Logic ----------------
#     if weapon_detected and aggressive_pose:
#         cv2.putText(frame, "HIGH RISK ALERT!", (50, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

#     elif weapon_detected:
#         cv2.putText(frame, "Weapon Detected!", (50, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

#     elif aggressive_pose:
#         cv2.putText(frame, "Suspicious Behavior!", (50, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 165, 255), 3)

#     # Show frame
#     cv2.imshow("Security System", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()