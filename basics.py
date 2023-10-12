import cv2


windowName = 'Image'
cv2.namedWindow(windowName)
cv2.moveWindow(windowName, 50,50)

img = cv2.imread('Pictures/Cat.png')
cv2.imshow(windowName, img)
cv2.waitKey(0)

# Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow(windowName, gray)
cv2.waitKey(0)

# Blur
blur = cv2.GaussianBlur(img, (3,3), cv2.BORDER_DEFAULT)
cv2.imshow(windowName, blur)
cv2.waitKey(0)

# Edge Cascade
canny = cv2.Canny(blur, 125, 175)
cv2.imshow(windowName, canny)
cv2.waitKey(0)

# Dilation
dilated = cv2.dilate(canny, (5,5), iterations=3)
cv2.imshow(windowName, dilated)
cv2.waitKey(0)

# Eroding
eroded = cv2.erode(dilated, (5,5), iterations=3)
cv2.imshow(windowName, eroded)
cv2.waitKey(0)

# Resize
resize = cv2.resize(img, (200,150), interpolation=cv2.INTER_CUBIC)
cv2.imshow(windowName, resize)
cv2.waitKey(0)

# Cropping
crop = img[60:190, 30:160]
cv2.imshow(windowName, crop)
cv2.waitKey(0)


cv2.destroyAllWindows()