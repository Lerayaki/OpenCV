import cv2
import numpy as np


def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    (h,w,_) = img.shape
    return cv2.warpAffine(img, transMat, (w,h))

def rotate(img, angle, point=None):
    (h,w,_) = img.shape

    if point is None:
        point = (w//2, h//2)
    
    rotMat = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(img, rotMat, (w,h))

windowName = 'Image'
cv2.namedWindow(windowName)
cv2.moveWindow(windowName, 50,50)

img = cv2.imread('Pictures/Cat.png')
cv2.imshow(windowName, img)
cv2.waitKey(0)

# Translation
cv2.imshow(windowName, translate(img, 150, 30))
cv2.waitKey(0)

# Rotation
cv2.imshow(windowName, rotate(img, 45))
cv2.waitKey(0)

# Resize
resize = cv2.resize(img, (600,450), interpolation=cv2.INTER_CUBIC)
cv2.imshow(windowName, resize)
cv2.waitKey(0)

# Flip
cv2.imshow(windowName, cv2.flip(img, 0))
cv2.waitKey(0)
cv2.imshow(windowName, cv2.flip(img, -1))
cv2.waitKey(0)

# Cropping
crop = img[60:190, 30:160]
cv2.imshow(windowName, crop)
cv2.waitKey(0)


cv2.destroyAllWindows()