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
#이미지의 폭, 높이, 컬러값을 해당 변수에 저장

matrix = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)
#.getRotationMatrix2D(Center, Angle, Scale)메서드
#회전행렬생성함수으로 회전 변환 행렬을 계산

#높이와 폭의 반은 이미지의 중심점이므로 이미지의 중심을 지정하고
#90도 회전
#이미지의 크기는 100% 유지

dst = cv2.warpAffine(src, matrix, (width, height))
#아핀 변환 함수으로 회전변환을 계산
#.wrapAffine(scr, M, dsize)메서드는 원본이미지(scr)에
#M(변환된 행렬)을 적용하고 이미지크기(dsize)를 적용하여
#입력 이미지를 변환한다

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(10000)
cv2.destroyAllWindows()