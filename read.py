import cv2

# Images
img = cv2.imread('Pictures/Cat.png')

cv2.namedWindow('Cat')
cv2.moveWindow('Cat', 0,0)
cv2.imshow('Cat', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('Pictures/Cat_HighRes.jpeg')

cv2.imshow('Cat', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Videos
cap = cv2.VideoCapture('Videos/Cat.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Video', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()

cv2.destroyAllWindows()