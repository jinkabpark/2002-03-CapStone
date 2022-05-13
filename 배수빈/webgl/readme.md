webGL in Raspberry 관련 issue 및 해결방안 작성초안 - by 배수빈

현재 라즈비안에서 webGl 호환성 issue가 많음
 - 같은 패키지/설정이여도 안되는 경우가 있음, system root 이나 레지스터리 수정 같은 고난이도 solution 필요
 - 22.05.13(금) 기준 
    1) 라즈베리3 +라즈비안os  + chrominium 브라우저에서 세팅 실패(webgl support 없다는 에러 확인)
    2) 라즈베리4 + Ubuntu Unity라는 오래된 실험 os의 firefox 브라우저로 실행 확인(초당 5~10프레임 나올까 말까)
      * 하지만 우분투 유니티 os는 서버 불안정 - 3일동안 받다가 파일 깨지고, torrent 다운로 어려운 상황
      * 
    
    5) 웹기반 브라우저 gpu 가속화 기능을 활용하기 때문에, 보다 높은 사양인 휴대폰, e북리더, 태블릿, pc 정상 작동 확인
    
https://drive.google.com/drive/folders/1GoiSDrv3Qu3fdNyOB4fb67RqxWkkka1e?usp=sharing
다운로드 완료한 ubuntu unity os 2종 image 파일 /webGL은 돌아가나, 라즈베리파이 자체 유니티 에디터는 지원하지 않음
(그래픽카드 요구치와, amdx64 기반 프로세서가 안되어서, 설치파일을 받아도, 라즈베리파이로 유니티를 직접 돌리는건 어려워 보임)

다른 방법으로는 안드로이드 os나 ios 운영체제로 설치후 빌드 하는방법이나, 이는 프로젝트에서 허가받지 못함

https://80000coding.oopy.io/ae4e684a-f9ec-48ef-be0d-e52f74ab627e
웹gl로 빌드한 유니티 게임 웹사이트로 배포하는법 참고(라즈베리파이로 unity 실행이나, 유니티-웹서버 사용 못할 때를 대비)

https://sbbae123.itch.io/webgl-uhouse-mk3
사이트 참고해가며 webgl 테스트 돌린 버전

pc 웹 브라우저 / 모바일(기본/크롬/카카오톡 링크 읽기) / 라즈베리파이4 ubuntu unity firefox 브라우저에서는 실행 확인

라즈비안 os 탑재한 라즈베리파이3 도 가능은 하나, 참고문헌과 사이트는 거의 2b와 3, 그리고 구버전 os 기준이라
설정이 어려움
 - https://get.webgl.org/ 해당 사이트에서 HW / SW 스펙으로는 실행 가능하다고 하나,
 - 실행시 의문의 에러로 WEBGL 지원 안한다는 문구 ( CHROMIUM 이외의 다른 브라우져 강구 필요)
