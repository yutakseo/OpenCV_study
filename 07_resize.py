import cv2

src = cv2.imread("lunar.jpg", cv2.IMREAD_COLOR)

dst_custom = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA)
dst_scale = cv2.resize(src, dsize=(640, 0),fx= 0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
#.resize(src, dstSize, fx, fy, interpolation)
#절대크기(dstSize)
#상대크기(fx, fy)
#보간법(interpolation) : 이미지의 크기가 변경되면 변형된 부분의 픽셀을 추정
#존재하지 않는 영역에 픽셀 값을 새로 매핑 or 압축
#보간법에 대한 추가 정보는 : https://076923.github.io/posts/Python-opencv-8/


cv2.imshow("src",src)
cv2.imshow("dst_custom",dst_custom)
cv2.imshow("dst_scale",dst_scale)
cv2.waitKey()
cv2.destroyAllWindows()