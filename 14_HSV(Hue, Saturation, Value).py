'''
색상(Hue) - 빨강, 노랑, 파랑 등으로 인식되는 색상 중 하나 또는 둘 이상의 색조합
과 같이 시각적 감각의 속성

채도(Saturation) - 이미지의 색상 깊이, 색상이 얼마나 순수한 색인지 의미

명도(Value) - 색의 밝고 어두운 정도를 의미
'''

import cv2

src = cv2.imread("tomato.jpg", cv2.IMREAD_UNCHANGED)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

cv2.imshow("h", h)
cv2.imshow("s", s)
cv2.imshow("v", v)

cv2.waitKey(10000)
cv2.destroyAllWindows()