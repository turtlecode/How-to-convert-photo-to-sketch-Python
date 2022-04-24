import cv2

image = cv2.imread("buffett.jpg")

grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

invet = cv2.bitwise_not(grey_img)

blur = cv2.GaussianBlur(invet, (21,21), 0)

invertedBlur = cv2.bitwise_not(blur)

sketch = cv2.divide(grey_img,invertedBlur, scale = 256.0)

cv2.imwrite("sketch.png", sketch)