# [project] 굿즈 마켓 플레이스 기획 - 3차

📅 2025-02-24

[원문 링크](https://code-chy.tistory.com/190)

---

<div class="area_view" id="article-view">
 <script async="" crossorigin="anonymous" onerror="changeAdsenseToAdfit()" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9527582522912841">
 </script>
 <!-- inventory -->
 <ins class="adsbygoogle" data-ad-adfit-unit="DAN-nRFiQiN4avFYIKbk" data-ad-client="ca-pub-9527582522912841" data-ad-format="auto" data-ad-slot="3825649038" data-ad-type="inventory" data-full-width-responsive="true" style="margin:50px 0; display:block">
 </ins>
 <script id="adsense_script">
  (adsbygoogle = window.adsbygoogle || []).push({});
 </script>
 <script>
  if(window.ObserveAdsenseUnfilledState !== undefined){ ObserveAdsenseUnfilledState(); }
 </script>
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
  <p data-ke-size="size16">
  </p>
  <h1>
   📝 [Project] MSA, TDD, 요구사항 및 DB 설계 정리
  </h1>
  <p data-ke-size="size16">
   📅
   <b>
    회의 날짜
   </b>
   : 2025. 2. 17.
  </p>
  <h2 data-ke-size="size26">
   🔥 최근 프로젝트 진행 상황
  </h2>
  <p data-ke-size="size16">
   요즘 일이 많아서 체력적으로도 힘들고, 요구사항도 끊임없이 쏟아지고 있어요... 🫠
   <br/>
   그래도 해야 할 일은 해야 하니까! 지난 회의 내용을 정리하면서 앞으로의 방향을 잡아보겠습니다.
  </p>
  <p data-ke-size="size16">
   &gt; 진짜 구라안치고 출근할 때마다 퇴사하겠다고 이야기 하는 듯 싶어요..
  </p>
  <hr data-ke-style="style1">
   <h2 data-ke-size="size26">
    ✅ 1. MSA 적용 여부
   </h2>
   <p data-ke-size="size16">
    <b>
     ❓ 우리가 MSA를 적용해야 할까?
    </b>
    <br/>
    현재 시스템 규모를 고려하면 MSA가 필수는 아니지만, 기술적 경험을 쌓기 위해 적용을 고민해봤어요.
   </p>
   <h3 data-ke-size="size23">
    🔹 데이터 처리 고민
   </h3>
   <p data-ke-size="size16">
    자주 호출되는 회원 정보 등은 어떻게 처리할까?
   </p>
   <p>
    <figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin" data-origin-height="199" data-origin-width="592">
     <span data-phocus="https://blog.kakaocdn.net/dn/bI22ww/btsMutHUW7N/ZDzUS5BuHYbVP1wKrjiIg1/img.png" data-url="https://blog.kakaocdn.net/dn/bI22ww/btsMutHUW7N/ZDzUS5BuHYbVP1wKrjiIg1/img.png">
      <img data-origin-height="199" data-origin-width="592" height="199" loading="lazy" onerror="this.onerror=null; this.src='//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png'; this.srcset='//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png';" src="https://blog.kakaocdn.net/dn/bI22ww/btsMutHUW7N/ZDzUS5BuHYbVP1wKrjiIg1/img.png" srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbI22ww%2FbtsMutHUW7N%2FZDzUS5BuHYbVP1wKrjiIg1%2Fimg.png" width="592"/>
     </span>
    </figure>
   </p>
   <ol data-ke-list-type="decimal" style="list-style-type: decimal;">
    <li>
     <b>
      중앙 Controller Server 및 DB를 통해 데이터 일괄 처리
     </b>
     <ul data-ke-list-type="disc" style="list-style-type: disc;">
      <li>
       ✅ 유지보수 용이
      </li>
      <li>
       ⚠️ 단일 장애점(SPOF) 발생 가능
      </li>
     </ul>
    </li>
    <li>
     <b>
      NoSQL 활용 → JSON 데이터 지속적 불러오기
     </b>
     <ul data-ke-list-type="disc" style="list-style-type: disc;">
      <li>
       ✅ 비정형 데이터 활용에 용이
      </li>
      <li>
       ⚠️ 트랜잭션 관리 어려움
      </li>
     </ul>
    </li>
   </ol>
   <p data-ke-size="size16">
    💡 현재
    <b>
     MVC 구조
    </b>
    로 시작하고, 추후
    <b>
     MSA 리팩토링을 고려
    </b>
    하기로 결정!
   </p>
   <hr data-ke-style="style1"/>
   <h2 data-ke-size="size26">
    ✅ 2. TDD 적용 여부
   </h2>
   <p data-ke-size="size16">
    TDD를 적용하면
    <b>
     코드 품질을 높일 수 있고, 이직에도 유리
    </b>
    하기 때문에 적극 활용해보기로 했어요.
   </p>
   <p data-ke-size="size16">
    🔹
    <b>
     Mockito / Mock 활용하여 테스트 코드 작성 연습
     <br/>
    </b>
    🔹
    <b>
     초기 개발 속도는 느려질 수 있지만, 장기적 유지보수성을 고려
    </b>
   </p>
   <p data-ke-size="size16">
    <b>
     <s>
      &gt; 사실 근데 그냥 내가 하고 싶어서 제안드렸어요(감사합니다 책임님..)
     </s>
    </b>
   </p>
   <hr data-ke-style="style1"/>
   <h2 data-ke-size="size26">
    ✅ 3. 요구사항 정리
   </h2>
   <p data-ke-size="size16">
    프로젝트의 핵심 기능을 정리하고,
    <b>
     우선순위를 명확히 설정
    </b>
    했어요.
    <br/>
    🚀
    <b>
     1차 목표
    </b>
    : 최소한의 기능을 구현(MVP) 후 인력 충원을 목표로!
   </p>
   <h3 data-ke-size="size23">
    🌟
    <b>
     핵심 기능 선정
    </b>
   </h3>
   <ol data-ke-list-type="decimal" style="list-style-type: decimal;">
    <li>
     <b>
      Auth(인증/인가) 시스템
     </b>
     - 담당:
     <ul data-ke-list-type="disc" style="list-style-type: disc;">
      <li>
       JWT, OAuth 적용 고려
      </li>
     </ul>
    </li>
    <li>
     <b>
      Commision(의뢰/수주 시스템)
     </b>
    </li>
    <li>
     <b>
      Payment(결제 시스템)
     </b>
    </li>
   </ol>
   <hr data-ke-style="style1"/>
   <h2 data-ke-size="size26">
    ✅ 4. DB 설계
   </h2>
   <h3 data-ke-size="size23">
    🛠️
    <b>
     4.1 Auth(인증/인가) DB 설계
    </b>
   </h3>
   <p data-ke-size="size16">
    ✔️
    <b>
     계정과 회원 정보를 분리하여 관리
    </b>
    하는 것이 확장성과 유지보수 측면에서 적절하다고 판단!
   </p>
   <p>
    <figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin" data-origin-height="514" data-origin-width="663">
     <span data-phocus="https://blog.kakaocdn.net/dn/bOD85I/btsMtoHnWK4/z84ChUrPpDsZ1itJRZWnWK/img.png" data-url="https://blog.kakaocdn.net/dn/bOD85I/btsMtoHnWK4/z84ChUrPpDsZ1itJRZWnWK/img.png">
      <img data-origin-height="514" data-origin-width="663" height="514" loading="lazy" onerror="this.onerror=null; this.src='//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png'; this.srcset='//t1.daumcdn.net/tistory_admin/static/images/no-image-v1.png';" src="https://blog.kakaocdn.net/dn/bOD85I/btsMtoHnWK4/z84ChUrPpDsZ1itJRZWnWK/img.png" srcset="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbOD85I%2FbtsMtoHnWK4%2Fz84ChUrPpDsZ1itJRZWnWK%2Fimg.png" width="663"/>
     </span>
    </figure>
   </p>
   <h4 data-ke-size="size20">
    📌
    <b>
     계정 테이블 (로그인 및 인증 담당)
    </b>
   </h4>
   <ul data-ke-list-type="disc" style="list-style-type: disc;">
    <li>
     <b>
      userID
     </b>
     (UUID, PK)
     <ul data-ke-list-type="disc" style="list-style-type: disc;">
      <li>
       사실 CUID도 고려 항목이다 보니... 무엇이 나을지 제안주셨음.. 좋겠다...
      </li>
     </ul>
    </li>
    <li>
     <b>
      로그인 계정 (email, kakao, naver 등)
     </b>
    </li>
    <li>
     <b>
      비밀번호
     </b>
    </li>
    <li>
     <b>
      OAuth 타입 (kakao, naver 등)
     </b>
    </li>
   </ul>
   <h4 data-ke-size="size20">
    📌
    <b>
     회원 정보 테이블 (프로필 및 권한 관리)
    </b>
   </h4>
   <ul data-ke-list-type="disc" style="list-style-type: disc;">
    <li>
     <b>
      userID (PK, FK)
     </b>
    </li>
    <li>
     <b>
      국가 코드, 닉네임, 이메일, 전화번호, 주소, 성별, 나이
     </b>
    </li>
    <li>
     <b>
      회원 상태 (status, enum 활용)
     </b>
     <b>
     </b>
    </li>
    <li>
     <b>
      인증 여부
     </b>
    </li>
   </ul>
   <p data-ke-size="size16">
    💡
    <b>
     팔로워/팔로잉 기능은 추후 확장 가능하도록 고려
    </b>
   </p>
   <p data-ke-size="size16">
    🥲사실 저와 책임님 둘 다 같은 회사다보니.. (둘 다 여기가 첫 회사..) 자꾸 DB에 모든 걸 다 때려박는 형식을 사용하려고 했거덩요..
    <br/>
    하지만 암만 생각해도 한
    <b>
     Table에 여러번 반복 조회가 될 것 같았고 이게 맞느냐?
    </b>
    라고 생각하면 아닐 것 같단말이져.. 이 때문에 enum으로 제안드렸어요
   </p>
   <hr data-ke-style="style1"/>
   <h3 data-ke-size="size23">
    🛠️
    <b>
     4.2 Commision(의뢰) DB 설계
    </b>
   </h3>
   <h4 data-ke-size="size20">
    📌
    <b>
     게시글 테이블
    </b>
   </h4>
   <ul data-ke-list-type="disc" style="list-style-type: disc;">
    <li>
     <b>
      title, content, writer, bookmark, timestamp, fileId
     </b>
    </li>
    <li>
     <b>
      파일 관리 방식 고민
      <br/>
     </b>
     🔹 file, fileType을 저장할지
     <br/>
     🔹 fileId 값만 관리하고 별도 file 테이블에서 관리할지
     <br/>
     ✅
     <b>
      결론
     </b>
     <span style="letter-spacing: 0px;">
      : fileId를 PK로 두고, fileType, file-url을 별도 테이블에서 관리하는 것이 적절
     </span>
     <ul data-ke-list-type="disc" style="list-style-type: disc;">
      <li>
       <span style="letter-spacing: 0px;">
        사실 애초에 file과 fileType만 있어도 table이 나뉘어질 것 같아.. 걍 fileId로 file이라는 table을 만들기루 결정~!
       </span>
      </li>
     </ul>
    </li>
   </ul>
   <h4 data-ke-size="size20">
    📌
    <b>
     Q&amp;A (문의) 테이블 &amp; 채팅 기능
    </b>
   </h4>
   <ul data-ke-list-type="disc" style="list-style-type: disc;">
    <li>
     <b>
      Q&amp;A ID, 글, usr1, usr2
     </b>
    </li>
    <li>
     WebSocket 활용하여 실시간 채팅 기능 구현 고려
    </li>
   </ul>
   <p data-ke-size="size16">
    💡
    <b>
     채팅 기능 상세 설계
    </b>
   </p>
   <ol data-ke-list-type="decimal" style="list-style-type: decimal;">
    <li>
     <b>
      ChatMembers 테이블
     </b>
     (채팅방 참여자 관리)
     <ul data-ke-list-type="disc" style="list-style-type: disc;">
      <li>
       <b>
        chatId, userId1, userId2
       </b>
      </li>
      <li>
       채팅 목록 UI에서 활용
      </li>
     </ul>
    </li>
    <li>
     <b>
      Messages 테이블
     </b>
     (채팅 메시지 저장)
     <ul data-ke-list-type="disc" style="list-style-type: disc;">
      <li>
       <b>
        chatId, messageType, timestamp, userId, msgId
       </b>
      </li>
      <li>
       트랜잭션 최적화 필요
      </li>
     </ul>
    </li>
   </ol>
   <p data-ke-size="size16">
    ⚠️
    <b>
     MessageStatus 테이블(읽음 상태 관리)은 업데이트 비용을 줄이기 위해 제외 검토
    </b>
   </p>
   <hr data-ke-style="style1"/>
   <h3 data-ke-size="size23">
    🛠️
    <b>
     4.3 Payment(결제) DB 설계
    </b>
   </h3>
   <p data-ke-size="size16">
    💡
    <b>
     에스크로(중간 보관) 시스템 도입 고민
    </b>
   </p>
   <ul data-ke-list-type="disc" style="list-style-type: disc;">
    <li>
     <b>
      구매자 → 에스크로 → 작업 완료 시 지급
     </b>
    </li>
    <li>
     사기 거래 방지를 위해 안전한 환경 구축 필수
     <ul data-ke-list-type="disc" style="list-style-type: disc;">
      <li>
       만약에 커미션주가.... 하청의 하청을 넣으면 어쩌지?
       <br/>
       ex)
       <a href="https://www.khan.co.kr/article/201301171351591" rel="noopener noreferrer" target="_blank">
        https://www.khan.co.kr/article/201301171351591
       </a>
      </li>
     </ul>
    </li>
   </ul>
   <figure contenteditable="false" data-ke-align="alignCenter" data-ke-type="opengraph" data-og-description="재택 근무의 허점을 이용해 자신의 일을 중국에 하청을 주고 근무 시간에 웹서핑만 해오던 미국의 한 회사원이 회사의 감사에 적발됐다. 소프트웨어 개발자인 40대 중반의 이 직원은 10만 달러 " data-og-host="www.khan.co.kr" data-og-image="https://scrap.kakaocdn.net/dn/bCXkjE/hyYjC0kY0X/DU7PyCtzK8RlDf5HN4ipN1/img.jpg?width=540&amp;height=371&amp;face=0_0_540_371,https://scrap.kakaocdn.net/dn/mJiwd/hyYjxrbUqa/Gq9JWPtcFXM0hcuPeyP8RK/img.jpg?width=540&amp;height=371&amp;face=0_0_540_371,https://scrap.kakaocdn.net/dn/rMPXf/hyYjKD3p5D/ztQpUMGvNCjGL3qHcP83V1/img.jpg?width=540&amp;height=371&amp;face=0_0_540_371" data-og-source-url="https://www.khan.co.kr/article/201301171351591" data-og-title="일하기 싫어 중국에 하청 준 미국 회사원" data-og-type="article" data-og-url="https://www.khan.co.kr/article/201301171351591" id="og_1740373793675">
    <a data-source-url="https://www.khan.co.kr/article/201301171351591" href="https://www.khan.co.kr/article/201301171351591" rel="noopener" target="_blank">
     <div class="og-image" style="background-image: url('https://scrap.kakaocdn.net/dn/bCXkjE/hyYjC0kY0X/DU7PyCtzK8RlDf5HN4ipN1/img.jpg?width=540&amp;height=371&amp;face=0_0_540_371,https://scrap.kakaocdn.net/dn/mJiwd/hyYjxrbUqa/Gq9JWPtcFXM0hcuPeyP8RK/img.jpg?width=540&amp;height=371&amp;face=0_0_540_371,https://scrap.kakaocdn.net/dn/rMPXf/hyYjKD3p5D/ztQpUMGvNCjGL3qHcP83V1/img.jpg?width=540&amp;height=371&amp;face=0_0_540_371');">
     </div>
     <div class="og-text">
      <p class="og-title" data-ke-size="size16">
       일하기 싫어 중국에 하청 준 미국 회사원
      </p>
      <p class="og-desc" data-ke-size="size16">
       재택 근무의 허점을 이용해 자신의 일을 중국에 하청을 주고 근무 시간에 웹서핑만 해오던 미국의 한 회사원이 회사의 감사에 적발됐다. 소프트웨어 개발자인 40대 중반의 이 직원은 10만 달러
      </p>
      <p class="og-host" data-ke-size="size16">
       www.khan.co.kr
      </p>
     </div>
    </a>
   </figure>
   <p data-ke-size="size16">
   </p>
   <p data-ke-size="size16">
    🚀
    <b>
     결제 API 연동 고려 사항
    </b>
    <br/>
    ✅
    <b>
     가상 캐시 충전 방식이 아닌 가입시 일정 금액 지급 방식
     <br/>
    </b>
    ✅
    <b>
     Open API 활용 (카카오페이, 네이버페이 연동 고려) -&gt; 충전가능형식으로 간다면!!
    </b>
   </p>
   <hr data-ke-style="style1"/>
   <h2 data-ke-size="size26">
    ✅ 5. 기술적 고민
   </h2>
   <h3 data-ke-size="size23">
    🤔
    <b>
     API 서버만 개발하는 방식?
    </b>
   </h3>
   <p data-ke-size="size16">
    기존에는 단일 서비스에서 모든 기능을 처리했지만, 확장성을 고려하여
    <br/>
    ✅
    <b>
     API 서버 &amp; 컨트롤러 서버 분리
    </b>
   </p>
   <ul data-ke-list-type="disc" style="list-style-type: disc;">
    <li>
     <b>
      API 서버
     </b>
     → 비즈니스 로직 담당
    </li>
    <li>
     <b>
      컨트롤러 서버
     </b>
     → 클라이언트(Web, Mobile)와 직접 소통
    </li>
   </ul>
   <p data-ke-size="size16">
    💡
    <b>
     이렇게 하면 여러 클라이언트에서 동일한 API 활용 가능!
     <br/>
     -&gt; 추후에 msa를 사용하게 된다면 이렇게 가지 않을까?
    </b>
   </p>
   <h3 data-ke-size="size23">
    🤔
    <b>
     공통 기능을 라이브러리화할까?
    </b>
   </h3>
   <p data-ke-size="size16">
    MSA 전환 가능성을 고려해
    <b>
     공통 기능을 .jar 형태로 관리
    </b>
    <br/>
    ✅
    <b>
     OAuth 2.0 / JWT 인증 모듈화
    </b>
    <br/>
    ✅
    <b>
     AOP 기반 로깅 및 예외 처리 적용
    </b>
    <br/>
    ✅
    <b>
     공통 결제 처리 모듈 구축
    </b>
   </p>
   <hr data-ke-style="style1"/>
   <h2 data-ke-size="size26">
    🚀
    <b>
     결론 및 향후 계획
    </b>
   </h2>
   <p data-ke-size="size16">
    여기까지 고민하는데 총 4시간 걸렸어요.. 사이드 프로젝트 기획은 정말정말정말.. 오래걸리고 즐겁고 힘겹네요ㅠ 책임님과 월화수목금토일 내내 마주하고 회의할 수 없나.. 엄청나게 고민되네요..,.
   </p>
   <p data-ke-size="size16">
    📌
    <b>
     우리가 배운 것!
    </b>
    <br/>
    ✅
    <b>
     API 서버와 컨트롤러 서버 분리 → 확장성과 유지보수성 향상
    </b>
    <br/>
    ✅
    <b>
     공통 기능 라이브러리화 → 중복 코드 감소, 서비스 일관성 유지
    </b>
    <br/>
    ✅
    <b>
     배치 프로그램 활용 → 반복 작업 자동화하여 운영 효율화
    </b>
    <br/>
    ✅
    <b>
     에스크로 결제 시스템 도입 → 안전한 거래 환경 구축
    </b>
   </p>
   <p data-ke-size="size16">
    📌
    <b>
     다음 단계
    </b>
   </p>
   <ol data-ke-list-type="decimal" style="list-style-type: decimal;">
    <li>
     API 설계 구체화
    </li>
    <li>
     DB 모델링 세부 정리
    </li>
    <li>
     MVP(최소 기능) 구축 후 테스트 진행 (이거.. 가능할까..?)
    </li>
   </ol>
   <p data-ke-size="size16">
   </p>
  </hr>
 </div>
 <!-- System - START -->
 <!-- System - END -->
 <div class="container_postbtn #post_button_group">
  <div class="postbtn_like">
   <script>
    window.ReactionButtonType = 'reaction';
window.ReactionApiUrl = '//code-chy.tistory.com/reaction';
window.ReactionReqBody = {
    entryId: 190
}
   </script>
   <div class="wrap_btn" data-tistory-react-app="Reaction" id="reaction-190">
   </div>
   <div class="wrap_btn wrap_btn_share">
    <button aria-expanded="false" class="btn_post sns_btn btn_share" data-blog-title="Cohe" data-description="📝 [Project] MSA, TDD, 요구사항 및 DB 설계 정리📅 회의 날짜: 2025. 2. 17.🔥 최근 프로젝트 진행 상황요즘 일이 많아서 체력적으로도 힘들고, 요구사항도 끊임없이 쏟아지고 있어요... 🫠그래도 해야 할 일은 해야 하니까! 지난 회의 내용을 정리하면서 앞으로의 방향을 잡아보겠습니다.&gt; 진짜 구라안치고 출근할 때마다 퇴사하겠다고 이야기 하는 듯 싶어요..✅ 1. MSA 적용 여부❓ 우리가 MSA를 적용해야 할까?현재 시스템 규모를 고려하면 MSA가 필수는 아니지만, 기술적 경험을 쌓기 위해 적용을 고민해봤어요.🔹 데이터 처리 고민자주 호출되는 회원 정보 등은 어떻게 처리할까?중앙 Controller Server 및 DB를 통해 데이터 일괄 처리✅ 유지보수 용이⚠️ 단일 장.." data-pc-url="https://code-chy.tistory.com/190" data-profile-image="https://tistory1.daumcdn.net/tistory/5646409/attach/8bf562b73e38446a9f0bb065fc30f867" data-profile-name="코헤0121" data-relative-pc-url="/190" data-thumbnail-url="https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&amp;fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbI22ww%2FbtsMutHUW7N%2FZDzUS5BuHYbVP1wKrjiIg1%2Fimg.png" data-title="[project] 굿즈 마켓 플레이스 기획 - 3차" type="button">
     <span class="ico_postbtn ico_share">
      공유하기
     </span>
    </button>
    <div class="layer_post" id="tistorySnsLayer">
    </div>
   </div>
   <div class="wrap_btn wrap_btn_etc" data-category-visibility="public" data-entry-id="190" data-entry-visibility="public">
    <button aria-expanded="false" class="btn_post btn_etc2" type="button">
     <span class="ico_postbtn ico_etc">
      게시글 관리
     </span>
    </button>
    <div class="layer_post" id="tistoryEtcLayer">
    </div>
   </div>
  </div>
  <button class="btn_menu_toolbar btn_subscription #subscribe" data-blog-id="5646409" data-device="web_pc" data-tiara-action-name="구독 버튼_클릭" data-url="https://code-chy.tistory.com/190" type="button">
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
   <a href="/category/%EC%82%AC%EC%9D%B4%EB%93%9C%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20%EC%9D%B4%EB%AA%A8%EC%A0%80%EB%AA%A8">
    사이드 프로젝트 이모저모
   </a>
   &gt;
   <a href="/category/%EC%82%AC%EC%9D%B4%EB%93%9C%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20%EC%9D%B4%EB%AA%A8%EC%A0%80%EB%AA%A8/%EA%B5%BF%EC%A6%88%20%EB%A7%88%EC%BC%93%ED%94%8C%EB%A0%88%EC%9D%B4%EC%8A%A4%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8">
    굿즈 마켓플레이스 프로젝트
   </a>
   ' 카테고리의 다른 글
  </h4>
  <table>
   <tr>
    <th>
     <a href="/195">
      [project] 굿즈 마켓 플레이스 기획 - 4차
     </a>
     <span>
      (0)
     </span>
    </th>
    <td>
     2025.03.06
    </td>
   </tr>
   <tr>
    <th>
     <a href="/189">
      [project] 굿즈 마켓 플레이스 기획 - 2차
     </a>
     <span>
      (1)
     </span>
    </th>
    <td>
     2025.02.20
    </td>
   </tr>
   <tr>
    <th>
     <a href="/188">
      [project] 굿즈 마켓 플레이스 기획 - 1차
     </a>
     <span>
      (0)
     </span>
    </th>
    <td>
     2025.02.18
    </td>
   </tr>
  </table>
 </div>
 <!-- PostListinCategory - END -->
</div>
