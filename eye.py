
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






