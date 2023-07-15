import cv2

src = cv2.imread("D:\image\Monarch_butterfly_in_Grand_Canary.jpg", cv2.IMREAD_UNCHANGED)
reflection = cv2.flip(src, 10)
#.flip 메서드는 이미지를 대칭할 수 있다 .flip(src, fip_code)
#flipCode < 0 xy축 대칭
#flipCode = 0 x축 대칭
#fipCode > 0 y축 대칭
#flipCode는 정수만으로 표현해야 한다


cv2.imshow("source", src)
cv2.imshow("reflection", reflection)

cv2.waitKey(5000)
cv2.destroyAllWindows()
