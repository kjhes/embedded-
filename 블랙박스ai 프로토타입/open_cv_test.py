# open_cv.py
# pip install opencv-python

import cv2
# print(cv2.__version__) 버전 체크:5.0.0

cap = cv2.VideoCapture()
# VideoCapture 클래스 : 카메라 또는 동영상 파일로 부터 특정 프레임을 받아올 수 있는 클래스

img = cv2.imread("cat.png") # 열 이미지 경로 지정
cv2.imshow("MY CAT",img) # 이미지 열기
cv2.waitKey(0)  # 키보드 입력 대기
cv2.destroyAllWindows() # 모든 창 닫기

b, g, r = cv2.split(img) # opencv 는 b g r 순서로 인식 rgb 아님
cv2.imshow("Red Channel", r)
cv2.imshow("Green Channel", g)
cv2.imshow("Blue Channel", b)

cv2.waitKey(0)