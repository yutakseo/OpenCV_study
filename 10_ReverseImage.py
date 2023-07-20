import cv2


#이미지 픽셀마다 비트연사을 not 연산 실행
# ex) 0b10 --> 1b01
src = cv2.imread("bird.jpg", cv2.IMREAD_COLOR)
dst = cv2.bitwise_not(src)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(5000)
cv2.destroyAllWindows()