#https://github.com/ONETAPL3G3ND
import cv2 
src = cv2.imread('D:/cv2-resize-image-original.png', cv2.IMREAD_UNCHANGED) 
# set a new height in pixels 
new_height = 200 
# dsize 
dsize = (src.shape[1], new_height)
# resize image 
output = cv2.resize(src, dsize, interpolation = cv2.INTER_AREA) 
cv2.imwrite('D:/cv2-resize-image-height.png',output)
Источник: https://tonais.ru/library/izmenenie-razmera-izobrazheniya-opencv-cv2-v-python
