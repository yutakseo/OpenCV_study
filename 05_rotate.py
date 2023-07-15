'''
회전은 선형변환 중 하나에 포함되며, 회전 변환 행렬을 통해 변환
회전 변환 행렬은 임의의 점을 중심으로 물체를 회전한다
회전변환 행렬의일부는 반사행렬과 같은 값을 지닐 수 있다
2차원 유클리드 공간에서의 회전은 크게 두가지로
좌표값을 회전시키는 회전행렬과 좌표축을 회전시키는 회전행렬
두 개가 있다
'''

import cv2

src = cv2.imread("bird.jpg", cv2.IMREAD_COLOR)


height, width, channel = src.shape
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
dst = cv2.warpAffine(src, matrix, (width, height))

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()