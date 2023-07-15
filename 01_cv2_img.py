import cv2

#cv2라이브러리가 이미지를 입력할 때는 .imgread 메서드를 사용한다
test_image = cv2.imread("D:\image\lunar.jpg", cv2.IMREAD_REDUCED_COLOR_2)

#.imgread(source, flags)

#source는 파일경로

#flags는 이미지의 초기 상태를 결정
'''
cv2.IMREAD_UNCHANGED : 원본 사용
cv2.IMREAD_GRAYSCALE : 1 채널, 그레이스케일 적용
cv2.IMREAD_COLOR : 3 채널, BGR 이미지 사용
cv2.IMREAD_ANYDEPTH : 이미지에 따라 정밀도를 16/32비트 또는 8비트로 사용
cv2.IMREAD_ANYCOLOR : 가능한 3 채널, 색상 이미지로 사용
cv2.IMREAD_REDUCED_GRAYSCALE_2 : 1 채널, 1/2 크기, 그레이스케일 적용
cv2.IMREAD_REDUCED_GRAYSCALE_4 : 1 채널, 1/4 크기, 그레이스케일 적용
cv2.IMREAD_REDUCED_GRAYSCALE_8 : 1 채널, 1/8 크기, 그레이스케일 적용
cv2.IMREAD_REDUCED_COLOR_2 : 3 채널, 1/2 크기, BGR 이미지 사용
cv2.IMREAD_REDUCED_COLOR_4 : 3 채널, 1/4 크기, BGR 이미지 사용
cv2.IMREAD_REDUCED_COLOR_8 : 3 채널, 1/8 크기, BGR 이미지 사용
'''
print(test_image.shape)
#이미지의 크기 출력 => 높이, 폭, 채널을 터미널에 출력


#이미지 출력함수
cv2.imshow("first CV", test_image)

#키 입력 대기함수
cv2.waitKey(2000)

#창 제거 함수
cv2.destroyWindow("first CV")