'''
색상(Hue) - 빨강, 노랑, 파랑 등으로 인식되는 색상 중 하나 또는 둘 이상의 색조합
과 같이 시각적 감각의 속성

채도(Saturation) - 이미지의 색상 깊이, 색상이 얼마나 순수한 색인지 의미

명도(Value) - 색의 밝고 어두운 정도를 의미
'''

import cv2

src = cv2.imread("Image/tomato.jpg", cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

h = cv2.inRange(h, 8, 20)
orange = cv2.bitwise_and(hsv, hsv, mask = h)
orange = cv2.cvtColor(orange, cv2.COLOR_HSV2BGR)
"""
Hue의 범위를 조정하여 특정 색상의 범위만 출력할 수 있습니다.

배열 요소의 범위 설정 함수(cv2.inRange)로 입력된 배열의 특정 범위 영역만 추출할 수 있습니다.

dst = cv2.inRange(src, lowerb, upperb)는 입력 이미지(src)의 낮은 범위(lowerb)에서 높은 범위(upperb) 사이의 요소를 추출합니다.

주황색은 약 8 ~ 20 범위를 갖습니다.

이후, 해당 추출한 영역을 마스크로 사용해 이미지 위에 덧씌워 해당 부분만 출력합니다.

비트 연산 AND(cv2.bitwise_and)로 간단하게 마스크를 덧씌울 수 있습니다.

dst = cv2.bitwise_and(src1, src2, mask)는 입력 이미지1(src1)과 입력 이미지2(src2)의 픽셀의 이진값이 동일한 영역만 AND 연산하여 반환합니다.

마스크 영역이 존재한다면 마스크 영역만 AND 연산을 진행합니다.

특정 영역(마스크)의 AND 연산이 완료됐다면 다시 HSV 색상 공간에서 BGR 색상 공간으로 변경합니다.
"""


cv2.imshow("orange", orange)
cv2.waitKey()
cv2.destroyAllWindows()