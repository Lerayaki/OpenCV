import cv2

def rescaleFrame(frame, scale=.75):
    (h,w,_) = frame.shape
    dimension = (int(w*scale), int(h*scale))
    return cv2.resize(frame, dimension, interpolation=cv2.INTER_AREA)


# Images
img = cv2.imread('Pictures/Cat.png')

cv2.namedWindow('Cat')
cv2.moveWindow('Cat', 50,50)
cv2.imshow('Cat', img)

cv2.namedWindow('Cat Resized')
cv2.moveWindow('Cat Resized', 500,50)
cv2.imshow('Cat Resized', rescaleFrame(img))
cv2.waitKey(0)
cv2.destroyAllWindows()

# Videos
cap = cv2.VideoCapture('Videos/Cat.mp4')

cv2.namedWindow('Video')
cv2.moveWindow('Video', 50,50)
cv2.namedWindow('Resized video')
cv2.moveWindow('Resized video', 1000,50)

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Video', frame)
        cv2.imshow('Resized video', rescaleFrame(frame, .5))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()

cv2.destroyAllWindows()