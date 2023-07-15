import cv2

capture = cv2.VideoCapture(0)
#비디오 출력 메서드, index번호를 통해 장치번호와 연결 내장카메라는 0, 그 외는 1~n

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
#카메라 속성 메서드, 속성과 값으로 표현

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    cv2.imshow("video frame", frame)
#반복문을 활용하여 카메라에서 프레임을 지속적으로 반영
#.waitKey 함수를 통해 지정된 시간 동안 프로그램을 대기
#.read 메서드를 통해 카메라 상태 및 프레임 입력
#ret은 카메라 상태 저장, 정상작동 = True, 비정상 = False로 반환
#frame에 현재 시점의 프레임이 저장

#.imshow(window_name, mat), mat은 이미지를 의미
 
capture.release()
#카메라 장치 메모리 해제
cv2.destroyAllWindows()
#모든 창 종료  