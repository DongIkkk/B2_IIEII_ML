IIEII 사물 인식 프로젝트
# **프로젝트 개요**

## 목표

- [실전 머신러닝]을 실습 하며 배운 머신러닝 기반으로 사물 분류 웹서비스 개발
- Django와 머신러닝을 활용하여 기한 내에 프로젝트 완성을 목표
- CNN/YOLO를 이용하여 이미지 분할(Segmentation)하는 과정 이해

## 주요 구현 기능

- 핵심 기능
    - 머신러닝
        - [사물 인식] 업로드 된 사진이 과일인지 아닌지 분류
        - 과일로 분류된 사진은 어떤 과일인지 분류
    - 장고
        - 사진 파일 업로드 기능 구현
        - 업로드된 사진 클릭하면 페이지 이동, 해당 이미지 카테고리 출력



## 아래 페이지를 클릭하시면 자세한 내용을 보실 수 있습니다.
https://www.notion.so/23c6d5761db74d08a24812972c9ba77a


## 진행상황

- 10/17(월)
    - 장고 : 사용자가 업로드한 파일 database에 업로드 한 뒤 가져오기 (이혜원)
         - 미해결 : 이미지 저장 및 호출은 되는데 사진으로 불러와지는게 아니라 경로'주소'가 불러와짐 
         

- 10/18(화)
    - 장고 : 미해결 부분 이미지 태그와 DTL사용해서 해결완료