# Pixel converter
이미지를 픽셀로 변환 후 색상 클러스터화하여 도트 그림처럼 보이게 합니다. 
아래 링크에서 실행중인 오픈소스 프로젝트 사용하였습니다.
[ドット絵こんばーた](https://app.monopro.org/pixel/)  

## 필수환경
- Python 3.x  
- Flask  
- Pillow  
- OpenCV  
- uWSGI(uWSGI에서 실행하는 경우)  

## 사용법
이미지를 업로드하고 조건을 설정한뒤 변환하면
기존 이미지가 가지고 있던 색상과 유사한 십자수 실의 색상으로 변환됩니다.

- 이미지 최대 크기 2mb
- 극단적인 비율의 이미지는 변환되지 않을 수 있음 ex) 세로로 긴 이미지 etc
- 배경이 없으면 좀 더 자세하게 묘사됨
- jpeg 파일을 사용하는 것을 권장함

## 핵심 기술
기존 오픈소스 프로젝트
- k-means 알고리즘
- Flask 서버
- REST API


변경사항
- 이미지 색상 변환
- AWS EC2
