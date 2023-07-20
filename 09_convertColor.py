"""
색상 공간 변환(Convert Color)은 본래의 색상 공간에서 다른 색상 공간으로 변환할 때 사용합니다.

색상 공간 변환 함수는 데이터 타입을 같게 유지하고 채널을 변환합니다.

입력된 이미지는 8 비트, 16 비트, 32 비트의 정밀도를 갖는 배열을 사용할 수 있습니다.

출력된 이미지는 입력된 이미지의 이미지 크기와 정밀도가 동일한 배열이 됩니다.

채널의 수가 감소하게 되어 이미지 내부의 데이터는 설정한 색상 공간과 일치하는 값으로 변환되며, 데이터 값이 변경되거나 채널 순서가 변경될 수 있습니다.


"""
import cv2

src = cv2.imread("bird.jpg", cv2.IMREAD_UNCHANGED)

dst = cv2.cvtColor(src,cv2.COLOR_BGR2RGB, None, None)
#.cvtColor(src, code, dst, dstCn)
# 색상변환코드(code) : BGR(RGB채널) ...
# 출력채널(dstCn) : 출력 이미지에 필요한 채널 수 설정
# CV_8U(0~255) / CV_16U(0~65535) / CV_32F(0~1)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(5000)
cv2.destroyAllWindows()
