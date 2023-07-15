import cv2

src = cv2.imread("D:\image\Monarch_butterfly_in_Grand_Canary.jpg", cv2.IMREAD_UNCHANGED)
reflection = cv2.flip(src, 0)



cv2.imshow("source", src)
cv2.imshow("reflection", reflection)

cv2.waitKey(5000)
cv2.destroyAllWindows()
