import cv2
import numpy as np

img = np.zeros((500,800,3), dtype='uint8')
img[:] = (207, 186, 95)
img[50:450, 50:750] = (186, 106, 44)

windowName = 'Image'
cv2.namedWindow(windowName)
cv2.moveWindow(windowName, 50,50)
cv2.imshow(windowName, img)
cv2.waitKey(0)

cv2.rectangle(img, (10,10), (790,490), (124,76,39), thickness=3)
cv2.circle(img, (400,250), radius=70, color=(200,200,200), thickness=cv2.FILLED)
cv2.rectangle(img, (370,230), (430,270), (213,235,175), thickness=cv2.FILLED)
cv2.line(img, (0,0), (800,500), color=(207, 186, 95), thickness=10)
cv2.putText(img, 'Some text...', (50,50), cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=2)
cv2.imshow(windowName, img)
cv2.waitKey(0)

cv2.destroyAllWindows()