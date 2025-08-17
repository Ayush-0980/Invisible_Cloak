import cv2
import numpy as np

cap = cv2.VideoCapture(0)
back = cv2.imread('./image.jpg')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Lower red range
    l_red = np.array([0, 120, 70])
    u_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, l_red, u_red)
    
    
    # Upper red range
    l_red2 = np.array([170, 120, 70])
    u_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, l_red2, u_red2)
    
    # Combine both masks
    mask = mask1 + mask2

    # Segment out the cloak from background image
    part1 = cv2.bitwise_and(back, back, mask=mask)
    
    # Create inverse mask for the original frame
    mask_inv = cv2.bitwise_not(mask)
    part2 = cv2.bitwise_and(frame, frame, mask=mask_inv)
    
    # Combine both to get the final output
    final = part1 + part2

    cv2.imshow("cloak", final)
    if cv2.waitKey(5) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
