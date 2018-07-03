# SmartCCTV_Server


PYTHON Flask Server for smartCCTV


OpenCV를 이용하여 이전에 감지되어 저장된 이미지와 유사도를 비교한다.

일정 수치보다 차이가 크다면 침입자로 판단 그렇지 않다면 등록된 사람이라고 판단한다.



1. 하드웨어 단에서는 카메라 모듈 + OpenCV를 이용하여 사람의 얼굴을 감지 ( HaarCascade ) 한다.

2. 유사도비교에 있어서 배경이나 색이 큰 영향을 끼치기 때문에 영향을 줄수 있는 배경 색과 배경을 자르고 

얼굴 부분만 잘라내어 전송한다.

3. Flask 서버에서는 OpenCV (SIFT_detector) 과  Histogram의 기반의 알고리즘을 이용하여 유사도를 비교한다.

4. 유사도의 threshold를 정하여 일정 수치가 초과한다면 침입자로 판단하여 하드웨어 부저로 알람을 준다. 



유사도 비교알고리즘

Main
![1](https://user-images.githubusercontent.com/28247914/42224611-820678a8-7f15-11e8-8bd6-f3421995535d.png)

저장된 이미지와 유사도 비교를 하여 침입자가 아니라고 판단
![2](https://user-images.githubusercontent.com/28247914/42224672-9b8c4352-7f15-11e8-9bf7-e0b58afaa750.png)


저장된 이미지와 유사도 비교를 하여 침입자라고 판단
![3](https://user-images.githubusercontent.com/28247914/42224676-9d1a169a-7f15-11e8-85a8-186fbdebaf16.png)
