import cv2
import numpy as np

# Open webcam (0 is usually the default camera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    height, width = frame.shape[:2]
    print(f"Frame size: {width}x{height}")
    
    # Drawing a Circle
    #cv2.line(image, start_point, radius, color, thickness)
    cv2.circle(frame, (320,240), 20, (0,0,255), 3)

    # Display the frame
    cv2.imshow('Webcam Feed', frame)
    

    # Break on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()