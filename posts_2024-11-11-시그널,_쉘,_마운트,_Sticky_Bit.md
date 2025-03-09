# 시그널, 쉘, 마운트, Sticky Bit

📅 2024-11-11

[원문 링크](https://code-chy.tistory.com/181)

---

<div class="area_view" id="article-view">
 <!-- System - START -->
 <div class="revenue_unit_wrap">
  <div class="revenue_unit_item adfit">
   <div class="revenue_unit_info">
    728x90
   </div>
   <ins class="kakao_ad_area" data-ad-height="90px" data-ad-unit="DAN-nP21vcNIK4cPjSVz" data-ad-width="728px" style="display: none;">
   </ins>
   <script async="async" src="//t1.daumcdn.net/kas/static/ba.min.js" type="text/javascript">
   </script>
  </div>
 </div>
 <!-- System - END -->
 <div class="contents_style">
  <h2 data-ke-size="size26">
   1. 주요 리눅스 시그널(Signal)
  </h2>
  <p data-ke-size="size16">
   리눅스에서 시그널은 프로세스 간 통신을 위한 중요한 메커니즘입니다. 주요 시그널들의 특징과 용도를 살펴보겠습니다.
   <br/>
   시그널(Signal)은 프로세스간 통신(IPC)을 위한 소프트웨어 인터럽트, 프로세스나 운영체제가 다른 프로세스에게 어떤 이벤트가 발생했음을 알리는 메커니즘.
  </p>
  <h3 data-ke-size="size23">
   쓰는 법
  </h3>
  <pre class="perl"><code># 프로세스 ID 확인
ps -ef | grep nginx

# nginx 설정 리로드
kill -1 `pidof nginx`

# 프로세스 상태 확인
ps aux | grep 1234

# 기본 문법
kill -[시그널번호] [프로세스ID]</code></pre>
  <h3 data-ke-size="size23">
   프로세스 제어 관련 시그널
  </h3>
  <ul data-ke-list-type="disc" style="list-style-type: disc;">
   <li>
    <b>
     SIGHUP(1)
    </b>
    : HangUP의 약자로, 터미널 연결이 끊어졌을 때 발생합니다. 데몬의 설정 파일을 다시 읽어들일 때도 사용됩니다.
   </li>
   <li>
    <b>
     SIGINT(2)
    </b>
    : 키보드에서 [CTRL]+[C]를 눌렀을 때 발생하는 인터럽트 시그널입니다.
   </li>
   <li>
    <b>
     SIGQUIT(3)
    </b>
    : [CTRL]+[]를 눌렀을 때 발생하며, 프로세스 종료 후 코어 덤프를 생성합니다.
   </li>
   <li>
    <b>
     SIGKILL(9)
    </b>
    : 가장 강력한 종료 시그널로, 프로세스를 즉시 강제 종료합니다.
   </li>
   <li>
    <b>
     SIGTERM(15)
    </b>
    : 정상적인 종료를 요청하는 시그널로, kill 명령의 기본값입니다.
   </li>
  </ul>
  <h3 data-ke-size="size23">
   오류 관련 시그널
  </h3>
  <ul data-ke-list-type="disc" style="list-style-type: disc;">
   <li>
    <b>
     SIGILL(4)
    </b>
    : 잘못된 명령어 실행 시 발생합니다.
   </li>
   <li>
    <b>
     SIGTRAP(5)
    </b>
    : 디버깅을 위한 중단점에서 발생합니다.
   </li>
   <li>
    <b>
     SIGABRT(6)
    </b>
    : abort() 함수 호출로 인한 비정상 종료 시 발생합니다.
   </li>
   <li>
    <b>
     SIGBUS(7)
    </b>
    : 메모리 접근 오류 시 발생합니다.
   </li>
   <li>
    <b>
     SIGSEGV(11)
    </b>
    : 잘못된 메모리 참조 시 발생합니다.
   </li>
  </ul>
  <h3 data-ke-size="size23">
   프로세스 상태 관련 시그널
  </h3>
  <ul data-ke-list-type="disc" style="list-style-type: disc;">
   <li>
    <b>
     SIGCHLD(17)
    </b>
    : 자식 프로세스가 중지되거나 종료될 때 부모 프로세스에게 전달됩니다.
   </li>
   <li>
    <b>
     SIGCONT(12)
    </b>
    : 중지된 프로세스를 다시 실행합니다.
   </li>
   <li>
    <b>
     SIGSTOP(19)
    </b>
    : 프로세스를 일시 중지시킵니다.
   </li>
   <li>
    <b>
     SIGTSTP(20)
    </b>
    : [CTRL]+[Z]를 눌렀을 때 발생하는 일시 중지 시그널입니다.
   </li>
  </ul>
  <h3 data-ke-size="size23">
   정리
  </h3>
  <p data-ke-size="size16">
  </p>
  <table border="1" data-ke-align="alignLeft" style="border-collapse: collapse; width: 100%; height: 624px;">
   <tbody>
    <tr style="height: 21px;">
     <td style="width: 6.04651%; height: 21px;">
      번호
     </td>
     <td style="width: 10.1163%; height: 21px;">
      이름
     </td>
     <td style="width: 72.4419%; height: 21px;">
      설명
     </td>
     <td style="width: 11.2791%; height: 21px;">
      기본처리
     </td>
    </tr>
    <tr style="height: 64px;">
     <td style="width: 6.04651%; height: 64px;">
      1
     </td>
     <td style="width: 10.1163%; height: 64px;">
      SIGHUP(HUP)
     </td>
     <td style="width: 72.4419%; height: 64px;">
      HangUP의 약어로 로그아웃과 같이 터미널에서 접속이 끊겼을 때 보내지는 시그널입니다. 데몬 관련 환경 설정 파일을 변경시키고 변화된 내용을 적용하기 위해 재시작할 때 이 시그널이 사용됩니다.
     </td>
     <td style="width: 11.2791%; height: 64px;">
      종료
     </td>
    </tr>
    <tr style="height: 35px;">
     <td style="width: 6.04651%; height: 35px;">
      2
     </td>
     <td style="width: 10.1163%; height: 35px;">
      SIGINT (INT)
     </td>
     <td style="width: 72.4419%; height: 35px;">
      키보드로부터 오는 인터럽트 시그널로 실행을 중지. [CTRL]+[c] 입력 시에 보내지는 시그널
     </td>
     <td style="width: 11.2791%; height: 35px;">
      종료
     </td>
    </tr>
    <tr style="height: 42px;">
     <td style="width: 6.04651%; height: 42px;">
      3
     </td>
     <td style="width: 10.1163%; height: 42px;">
      SIGQUIT (QUIT)
     </td>
     <td style="width: 72.4419%; height: 42px;">
      키보드로부터 오는 실행 중지 시그널 [CTRL] + [\] 입력 시에 보내지는 시그널입니다. 기본적으로 프로세스를 종료시킨 뒤 코어를 덤프하는 역할을 함.
     </td>
     <td style="width: 11.2791%; height: 42px;">
      코어덤프
     </td>
    </tr>
    <tr style="height: 35px;">
     <td style="width: 6.04651%; height: 35px;">
      4
     </td>
     <td style="width: 10.1163%; height: 35px;">
      SIGILL (ILL)
     </td>
     <td style="width: 72.4419%; height: 35px;">
      illegal instruction의 약자입니다. 잘못된 명령을 사용했을 때 발생합니다.
     </td>
     <td style="width: 11.2791%; height: 35px;">
      코어덤프
     </td>
    </tr>
    <tr style="height: 35px;">
     <td style="width: 6.04651%; height: 35px;">
      5
     </td>
     <td style="width: 10.1163%; height: 35px;">
      SIGTRAP (TRAP)
     </td>
     <td style="width: 72.4419%; height: 35px;">
      trace(추적), breakpoint(중지점)에서 TRAP 발생할 때
     </td>
     <td style="width: 11.2791%; height: 35px;">
      코어덤프
     </td>
    </tr>
    <tr style="height: 42px;">
     <td style="width: 6.04651%; height: 42px;">
      6
     </td>
     <td style="width: 10.1163%; height: 42px;">
      SIGABRT (ABRT)
     </td>
     <td style="width: 72.4419%; height: 42px;">
      abort의 약자로 비정상종료 함수에 의해 발생합니다. (즉 abort 시스템 호출을 하였을 때 발생)
     </td>
     <td style="width: 11.2791%; height: 42px;">
      코어덤프
     </td>
    </tr>
    <tr style="height: 21px;">
     <td style="width: 6.04651%; height: 21px;">
      7
     </td>
     <td style="width: 10.1163%; height: 21px;">
      SIGBUS
     </td>
     <td style="width: 72.4419%; height: 21px;">
      메모리 접근 에러시 발생하는 시그널입니다.
     </td>
     <td style="width: 11.2791%; height: 21px;">
      코어덤프
     </td>
    </tr>
    <tr style="height: 56px;">
     <td style="width: 6.04651%; height: 56px;">
      9
     </td>
     <td style="width: 10.1163%; height: 56px;">
      SIGKILL (KILL) ⇒ kill -9
     </td>
     <td style="width: 72.4419%; height: 56px;">
      KILL! 무조건 종료, 즉 프로세스를 강제로 종료시키는 시그널!
     </td>
     <td style="width: 11.2791%; height: 56px;">
      종료
     </td>
    </tr>
    <tr style="height: 42px;">
     <td style="width: 6.04651%; height: 42px;">
      11
     </td>
     <td style="width: 10.1163%; height: 42px;">
      SIGSEGV
     </td>
     <td style="width: 72.4419%; height: 42px;">
      invalid memory reference
     </td>
     <td style="width: 11.2791%; height: 42px;">
      종료 + 코어덤프
     </td>
    </tr>
    <tr style="height: 56px;">
     <td style="width: 6.04651%; height: 56px;">
      15
     </td>
     <td style="width: 10.1163%; height: 56px;">
      SIGTERM(TERM) ⇒ kill -15
     </td>
     <td style="width: 72.4419%; height: 56px;">
      Terminate의 약자로 가능한 정상 종료시키는 시그널로 kill 명령의 기본 시그널입니다.
     </td>
     <td style="width: 11.2791%; height: 56px;">
      종료
     </td>
    </tr>
    <tr style="height: 42px;">
     <td style="width: 6.04651%; height: 42px;">
      17
     </td>
     <td style="width: 10.1163%; height: 42px;">
      SIGCHLD (child)
     </td>
     <td style="width: 72.4419%; height: 42px;">
      자식 프로세스가 stop 되거나 종료되었을 때 부모에게 전달되는 신호입니다. (멀티 프로세스 코딩에서 자세한 사용법은 배울 거..)
     </td>
     <td style="width: 11.2791%; height: 42px;">
      무시
     </td>
    </tr>
    <tr style="height: 35px;">
     <td style="width: 6.04651%; height: 35px;">
      12
     </td>
     <td style="width: 10.1163%; height: 35px;">
      SIGCONT (CONT)
     </td>
     <td style="width: 72.4419%; height: 35px;">
      Continue의 약자로 STOP 시그널에 의해 정지된 프로세스를 다시 실행시킬 때 사용됩니다.
     </td>
     <td style="width: 11.2791%; height: 35px;">
      재시작
     </td>
    </tr>
    <tr style="height: 35px;">
     <td style="width: 6.04651%; height: 35px;">
      19
     </td>
     <td style="width: 10.1163%; height: 35px;">
      SIGSTOP (STOP)
     </td>
     <td style="width: 72.4419%; height: 35px;">
      터미널에서 입력된 정지 시그널입니다. SIGCONT로 재실행시킬 수 있습니다.
     </td>
     <td style="width: 11.2791%; height: 35px;">
      중지
     </td>
    </tr>
    <tr style="height: 42px;">
     <td style="width: 6.04651%; height: 42px;">
      20
     </td>
     <td style="width: 10.1163%; height: 42px;">
      SIGTSTP (TSTP)
     </td>
     <td style="width: 72.4419%; height: 42px;">
      실행 정지 후 다시 실행을 계속하기 위해 대기시키는 시그널입니다. [CTRL] + [z]를 입력했을 때 보내지는 시그널입니다. SIGCONT로 역시 다시 실행시킬 수 있습니다.
     </td>
     <td style="width: 11.2791%; height: 42px;">
      중지
     </td>
    </tr>
    <tr style="height: 21px;">
     <td style="width: 6.04651%; height: 21px;">
      29
     </td>
     <td style="width: 10.1163%; height: 21px;">
      SIGIO
     </td>
     <td style="width: 72.4419%; height: 21px;">
      비동기 입출력이 발생했을 경우 ! (I/O now possible!)
     </td>
     <td style="width: 11.2791%; height: 21px;">
      종료
     </td>
    </tr>
   </tbody>
  </table>
  <p data-ke-size="size16">
  </p>
  <h2 data-ke-size="size26">
   2. 리눅스 쉘의 진화
  </h2>
  <p data-ke-size="size16">
   쉘은 사용자와 커널 사이의 인터페이스 역할을 하는 중요한 프로그램입니다. 시간의 흐름에 따라 다양한 쉘이 개발되었습니다.
  </p>
  <h3 data-ke-size="size23">
   쉘의 발전 과정
  </h3>
  <ol data-ke-list-type="decimal" style="list-style-type: decimal;">
   <li>
    <b>
     sh (Bourne Shell)
    </b>
    <ul data-ke-list-type="disc" style="list-style-type: disc;">
     <li>
      최초로 개발된 POSIX 호환 쉘
     </li>
     <li>
      기본적인 쉘 기능 제공
     </li>
    </ul>
   </li>
   <li>
    <b>
     csh (C Shell)
    </b>
    <ul data-ke-list-type="disc" style="list-style-type: disc;">
     <li>
      1978년 빌 조이가 개발
     </li>
     <li>
      C 언어 기반의 문법 채택
     </li>
     <li>
      히스토리, alias 기능 도입
     </li>
    </ul>
   </li>
   <li>
    <b>
     tcsh
    </b>
    <ul data-ke-list-type="disc" style="list-style-type: disc;">
     <li>
      C 쉘의 확장판
     </li>
     <li>
      명령줄 완성, 편집 기능 강화
     </li>
    </ul>
   </li>
   <li>
    <b>
     ksh (Korn Shell)
    </b>
    <ul data-ke-list-type="disc" style="list-style-type: disc;">
     <li>
      유닉스 환경에서 널리 사용
     </li>
     <li>
      Bourne 쉘과의 호환성 유지
     </li>
     <li>
      향상된 명령행 편집 기능
     </li>
    </ul>
   </li>
   <li>
    <b>
     bash (Bourne Again Shell)
    </b>
    <ul data-ke-list-type="disc" style="list-style-type: disc;">
     <li>
      GNU 프로젝트의 일환으로 개발
     </li>
     <li>
      현재 리눅스의 대표적인 쉘
     </li>
     <li>
      강력한 스크립팅 기능 제공
     </li>
    </ul>
   </li>
   <li>
    <b>
     zsh
    </b>
    <ul data-ke-list-type="disc" style="list-style-type: disc;">
     <li>
      최신 기능들을 통합한 현대적인 쉘
     </li>
     <li>
      높은 확장성과 커스터마이징 가능
     </li>
    </ul>
   </li>
  </ol>
  <h2 data-ke-size="size26">
   3. 파일시스템 마운트 옵션
  </h2>
  <p data-ke-size="size16">
   리눅스에서 다양한 저장 장치와 네트워크 파일시스템을 마운트할 때 사용되는 주요 옵션들입니다.
  </p>
  <h3 data-ke-size="size23">
   주요 마운트 타입
  </h3>
  <ul data-ke-list-type="disc" style="list-style-type: disc;">
   <li>
    <b>
     nfs
    </b>
    : 네트워크 파일시스템 프로토콜
   </li>
   <li>
    <b>
     udf
    </b>
    : 범용 디스크 포맷 (광학 미디어용)
   </li>
   <li>
    <b>
     cifs
    </b>
    : 윈도우즈와의 호환성을 위한 네트워크 파일시스템
   </li>
   <li>
    <b>
     iso9660
    </b>
    : CD-ROM 표준 파일시스템
   </li>
   <li>
    <b>
     loop
    </b>
    : ISO 이미지 파일을 마운트할 때 사용
   </li>
  </ul>
  <h2 data-ke-size="size26">
   4. 특수 권한: Sticky Bit
  </h2>
  <p data-ke-size="size16">
   디렉토리에 설정하는 특수 권한인 sticky bit는 공유 디렉토리에서 사용자들의 파일을 보호하는 중요한 보안 기능을 제공합니다. 주로 /tmp나 /var/tmp와 같은 공용 디렉토리에서 사용됩니다.
  </p>
 </div>
 <!-- System - START -->
 <!-- System - END -->
 <script async="" crossorigin="anonymous" onerror="changeAdsenseToAdfit()" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9527582522912841">
 </script>
 <!-- inventory -->
 <ins class="adsbygoogle" data-ad-adfit-unit="DAN-HCZEy0KQLPMGnGuC" data-ad-client="ca-pub-9527582522912841" data-ad-format="auto" data-ad-slot="4947159016" data-ad-type="inventory" data-full-width-responsive="true" style="margin:50px 0; display:block">
 </ins>
 <script id="adsense_script">
  (adsbygoogle = window.adsbygoogle || []).push({});
 </script>
 <script>
  if(window.ObserveAdsenseUnfilledState !== undefined){ ObserveAdsenseUnfilledState(); }
 </script>
 <div class="container_postbtn #post_button_group">
  <div class="postbtn_like">
   <script>
    window.ReactionButtonType = 'reaction';
window.ReactionApiUrl = '//code-chy.tistory.com/reaction';
window.ReactionReqBody = {
    entryId: 181
}
   </script>
   <div class="wrap_btn" data-tistory-react-app="Reaction" id="reaction-181">
   </div>
   <div class="wrap_btn wrap_btn_share">
    <button aria-expanded="false" class="btn_post sns_btn btn_share" data-blog-title="Cohe" data-description="1. 주요 리눅스 시그널(Signal)리눅스에서 시그널은 프로세스 간 통신을 위한 중요한 메커니즘입니다. 주요 시그널들의 특징과 용도를 살펴보겠습니다.시그널(Signal)은 프로세스간 통신(IPC)을 위한 소프트웨어 인터럽트, 프로세스나 운영체제가 다른 프로세스에게 어떤 이벤트가 발생했음을 알리는 메커니즘.쓰는 법# 프로세스 ID 확인ps -ef | grep nginx# nginx 설정 리로드kill -1 `pidof nginx`# 프로세스 상태 확인ps aux | grep 1234# 기본 문법kill -[시그널번호] [프로세스ID]프로세스 제어 관련 시그널SIGHUP(1): HangUP의 약자로, 터미널 연결이 끊어졌을 때 발생합니다. 데몬의 설정 파일을 다시 읽어들일 때도 사용됩니다.SIGINT(2).." data-pc-url="https://code-chy.tistory.com/181" data-profile-image="https://tistory1.daumcdn.net/tistory/5646409/attach/8bf562b73e38446a9f0bb065fc30f867" data-profile-name="코헤0121" data-relative-pc-url="/181" data-thumbnail-url="https://t1.daumcdn.net/tistory_admin/static/images/openGraph/opengraph.png" data-title="시그널, 쉘, 마운트, Sticky Bit" type="button">
     <span class="ico_postbtn ico_share">
      공유하기
     </span>
    </button>
    <div class="layer_post" id="tistorySnsLayer">
    </div>
   </div>
   <div class="wrap_btn wrap_btn_etc" data-category-visibility="public" data-entry-id="181" data-entry-visibility="public">
    <button aria-expanded="false" class="btn_post btn_etc2" type="button">
     <span class="ico_postbtn ico_etc">
      게시글 관리
     </span>
    </button>
    <div class="layer_post" id="tistoryEtcLayer">
    </div>
   </div>
  </div>
  <button class="btn_menu_toolbar btn_subscription #subscribe" data-blog-id="5646409" data-device="web_pc" data-tiara-action-name="구독 버튼_클릭" data-url="https://code-chy.tistory.com/181" type="button">
   <em class="txt_state">
   </em>
   <strong class="txt_tool_id">
    Cohe
   </strong>
   <span class="img_common_tistory ico_check_type1">
   </span>
  </button>
  <div class="postbtn_ccl" data-ccl-derive="1" data-ccl-type="6">
   <a class="link_ccl" href="https://creativecommons.org/licenses/by-nc/4.0/deed.ko" rel="license" target="_blank">
    <span class="bundle_ccl">
     <span class="ico_postbtn ico_ccl1">
      저작자표시
     </span>
     <span class="ico_postbtn ico_ccl2">
      비영리
     </span>
    </span>
   </a>
  </div>
  <!--
            <rdf:RDF xmlns="https://web.resource.org/cc/" xmlns:dc="https://purl.org/dc/elements/1.1/" xmlns:rdf="https://www.w3.org/1999/02/22-rdf-syntax-ns#">
                <Work rdf:about="">
                    <license rdf:resource="https://creativecommons.org/licenses/by-nc/4.0/deed.ko" />
                </Work>
                <License rdf:about="https://creativecommons.org/licenses/by-nc/4.0/deed.ko">
                    <permits rdf:resource="https://web.resource.org/cc/Reproduction"/>
                    <permits rdf:resource="https://web.resource.org/cc/Distribution"/>
                    <requires rdf:resource="https://web.resource.org/cc/Notice"/>
                    <requires rdf:resource="https://web.resource.org/cc/Attribution"/>
                    <permits rdf:resource="https://web.resource.org/cc/DerivativeWorks"/>
<prohibits rdf:resource="https://web.resource.org/cc/CommercialUse"/>

                </License>
            </rdf:RDF>
            -->
  <div data-tistory-react-app="SupportButton">
  </div>
 </div>
 <!-- PostListinCategory - START -->
 <div class="another_category another_category_color_gray">
  <h4>
   '
   <a href="/category/%EC%9E%90%EA%B2%A9%EC%A6%9D%20%EA%B3%B5%EB%B6%80">
    자격증 공부
   </a>
   &gt;
   <a href="/category/%EC%9E%90%EA%B2%A9%EC%A6%9D%20%EA%B3%B5%EB%B6%80/%EB%A6%AC%EB%88%85%EC%8A%A4%20%EB%A7%88%EC%8A%A4%ED%84%B0%202%EA%B8%89">
    리눅스 마스터 2급
   </a>
   ' 카테고리의 다른 글
  </h4>
  <table>
   <tr>
    <th>
     <a href="/187">
      리눅스마스터 2급 20231209 오답 1
     </a>
     <span>
      (0)
     </span>
    </th>
    <td>
     2024.11.30
    </td>
   </tr>
   <tr>
    <th>
     <a href="/185">
      리눅스 시스템 관리 - 프로세스 관리와 편집기
     </a>
     <span>
      (0)
     </span>
    </th>
    <td>
     2024.11.16
    </td>
   </tr>
   <tr>
    <th>
     <a href="/184">
      리눅스 권한
     </a>
     <span>
      (1)
     </span>
    </th>
    <td>
     2024.11.13
    </td>
   </tr>
   <tr>
    <th>
     <a href="/183">
      du/df, mkfs, 파티션 ID, fsck
     </a>
     <span>
      (2)
     </span>
    </th>
    <td>
     2024.11.12
    </td>
   </tr>
  </table>
 </div>
 <!-- PostListinCategory - END -->
</div>
