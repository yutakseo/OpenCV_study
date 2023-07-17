import cv2

src = cv2.imread('lunar.jpg', cv2.IMREAD_UNCHANGED)

height, width, channel = src.shape

dstUP = cv2.pyrUp(src, dstsize=(width*2, height*2), borderType=cv2.BORDER_DEFAULT)
dstDown = cv2.pyrDown(src)
#가우시안 피라미드 법을 이용해 이미지의 사이즈를 변경한다
#정확한 내용의 이해는 추가적인 공부가 필요할 것 같다

cv2.imshow("src", src)
cv2.imshow("dstUP",dstUP)
cv2.imshow("dstDown",dstDown)

cv2.waitKey(0)
cv2.destroyAllWindows
