webGL in Raspberry 관련 issue 및 해결방안 작성초안 - by 배수빈

현재 라즈비안에서 webGl 호환성 issue가 많음
 - 같은 패키지/설정이여도 안되는 경우가 있음, system root 이나 레지스터리 수정 같은 고난이도 solution 필요
 - 22.05.13(금) 기준 
    1) 라즈베리3 +라즈비안os  + chrominium 브라우저에서 세팅 실패(webgl support 없다는 에러 확인)
    2) 라즈베리4 + Ubuntu Unity라는 오래된 실험 os의 firefox 브라우저로 실행 확인(초당 5~10프레임 나올까 말까)
      * 하지만 우분투 유니티 os는 서버 불안정 - 3일동안 받다가 파일 깨지고, torrent 다운로 어려운 상황
      * 
    
    5) 웹기반 브라우저 gpu 가속화 기능을 활용하기 때문에, 보다 높은 사양인 휴대폰, e북리더, 태블릿, pc 정상 작동 확인
    


https://80000coding.oopy.io/ae4e684a-f9ec-48ef-be0d-e52f74ab627e
웹gl로 빌드한 유니티 게임 웹사이트로 배포하는법(웹서버 사용 못할 때를 대비)

