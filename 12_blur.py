import cv2

src = cv2.imread("bird.jpg", cv2.IMREAD_UNCHANGED)
dst = cv2.blur(src, (55,55), anchor=(27, 27), borderType=cv2.BORDER_DEFAULT)
#.blur(src, ksize, anchor, borderType)
#커널크기(ksize), 한 픽셀에서 주변을 포함한 공간 여기서는 9*9
#고정점(anchor), 커널 내부에서 존재하는 중앙점
#커널을 통한 컨벌루션 계산을 하게되면 필터 가장자리를 어떻게 처리할 것인가


cv2.imshow("dst", dst)
cv2.waitKey(10000)
cv2.destroyAllWindows()

