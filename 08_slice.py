import cv2

src = cv2.imread("bird.jpg", cv2.IMREAD_COLOR)

dst = src[100:600, 200:700].copy()
#scr[높이(행), 너비(열)]
#.copy() ==> 이미지 복사

cv2.imshow("src",src)
cv2.imshow("dst",dst)

cv2.waitKey(5000)
cv2.destroyAllWindows()

