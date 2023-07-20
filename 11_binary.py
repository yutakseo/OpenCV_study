import cv2

src = cv2.imread("bird.jpg", cv2.IMREAD_UNCHANGED)

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, dst = cv2.threshold(gray, 100, 150, cv2.THRESH_BINARY)
#이진화를 하려면 흰색과 검은색의 흑백사진을 가지고 이진화를 시킨다
#.threshold(src, thresh, maxval, type)
#입력이미지(src)
#임계값(thresh) : 이 값보다 픽셀 값이 크면 해당 픽셀을 최대값으로 변환
#최대값(maxval) : 임계값을 넘으면 변환하는 값



cv2.imshow("dst", dst)
cv2.waitKey(5000)
cv2.destroyAllWindows()