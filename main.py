import numpy as np
import cv2
bgr = cv2.imread('image-input.jpd')
lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
lab_planes = cv2.split(lab)
clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
lab_planes[0] = clahe.apply(lab_planes[0])
lab = cv2.merge(lab_planes)
bgr = cv2.cvtColor(lab, cv2.COLOR_GRAY2BGR)
cv2.imwrite('img-output.jpg',bgr)
