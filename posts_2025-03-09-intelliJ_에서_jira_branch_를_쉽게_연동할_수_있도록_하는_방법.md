# intelliJ 에서 jira branch 를 쉽게 연동할 수 있도록 하는 방법

📅 2025-03-09

[원문 링크](https://code-chy.tistory.com/197)

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
  <h3 data-ke-size="size23">
   ✨ 개념 설명
  </h3>
  <p data-ke-size="size16">
   지라로 협업툴을 사용하게 되며
  </p>
  <ol data-ke-list-type="decimal" style="list-style-type: decimal;">
   <li>
    브랜치 생성
   </li>
   <li>
    코드 작성
   </li>
   <li>
    PR
    <br/>
    이 순 중 브랜치 생성을 수월하게 하기 위해 아래와 같은 내용을 따라하길 권장
   </li>
  </ol>
  <hr data-ke-style="style1">
   <h2 data-ke-size="size26">
    🛠️ 사용 방법
   </h2>
   <p data-ke-size="size16">
    우리는 크게 2가지를 신경 쓸 것이다.
   </p>
   <ol data-ke-list-type="decimal" style="list-style-type: decimal;">
    <li>
     JIRA에서 로그인을 위한 API 들고오기
    </li>
    <li>
     intelliJ에서 jira 연동하기
    </li>
   </ol>
   <h3 data-ke-size="size23">
    1. JIRA에서 로그인을 위한 API 들고오기
   </h3>
   <ol data-ke-list-type="decimal" style="list-style-type: decimal;">
    <li>
     계정 관리를 찾아 클릭한다
    </li>
   </ol>
   <ul data-ke-list-type="disc" style="list-style-type: disc;">
    <li>
     프로필을 찾아 계정 관리를 클릭한다
    </li>
   </ul>
   <p>
    <img alt="Image" src="https://github.com/user-attachments/assets/999f1a82-a305-4a76-afae-0d853599fb72"/>
   </p>
   <ol data-ke-list-type="decimal" start="2" style="list-style-type: decimal;">
    <li>
     그럼 아래와 같은 화면이 나오는데 보안 탭을 클릭하여 API 토큰을 클릭해봅시다
    </li>
   </ol>
   <p>
    <img alt="Image" src="https://github.com/user-attachments/assets/f71043e0-2e14-467f-b724-835653de9b47"/>
   </p>
   <ol data-ke-list-type="decimal" start="3" style="list-style-type: decimal;">
    <li>
     그럼 이런 창이 뜨는데 API 토큰을 만들어 줍시다
    </li>
   </ol>
   <p>
    <img alt="Image" src="https://github.com/user-attachments/assets/cc92d176-4bf3-4b20-b3e7-5caf34a61340"/>
    <img alt="Image" src="https://github.com/user-attachments/assets/527f40e0-dc32-4072-a54a-400ad0f545a9"/>
   </p>
   <ol data-ke-list-type="decimal" start="4" style="list-style-type: decimal;">
    <li>
     API 토큰을 복사하고
    </li>
   </ol>
   <p>
    <img alt="Image" src="https://github.com/user-attachments/assets/29ed8f16-ec5a-40f5-9d6c-e50955fcb3cd"/>
   </p>
   <p data-ke-size="size16">
    고생 많으셨습니다 이제 인텔리제이로 넘어갑시다
   </p>
   <h3 data-ke-size="size23">
    2. intelliJ에서 jira 연동하기
   </h3>
   <ol data-ke-list-type="decimal" style="list-style-type: decimal;">
    <li>
     jira plugin을 추가한다
    </li>
   </ol>
   <p>
    <img alt="Image" src="https://github.com/user-attachments/assets/06928596-9fb8-4b3c-a919-51d67e30918b"/>
   </p>
   <ol data-ke-list-type="decimal" start="2" style="list-style-type: decimal;">
    <li>
     다운이 다 되면 아래와 같은게 뜨는데, 클릭하여 -&gt; Configure를 클릭한다.
    </li>
   </ol>
   <p>
    <img alt="Image" src="https://github.com/user-attachments/assets/f53f67b5-9ca6-43cf-a985-13f885667b36"/>
   </p>
   <ol data-ke-list-type="decimal" start="3" style="list-style-type: decimal;">
    <li>
     그럼 이런 창이 뜨는데
    </li>
   </ol>
   <ul data-ke-list-type="disc" style="list-style-type: disc;">
    <li>
     버튼을 누릅니다
     <br/>
     server url :
     <a href="https://ducks25.atlassian.net/">
      https://ducks25.atlassian.net/
     </a>
     <br/>
     email : 자신의 atlassian 계정
     <br/>
     API : 위에서 받아온 토큰 (잃어버렸으면 다시 작업하여 토큰 재발행이 가능합니다.)
    </li>
   </ul>
   <p>
    <img alt="Image" src="https://github.com/user-attachments/assets/fab750b2-b1eb-419f-b711-dd0d2f58cf1e"/>
   </p>
   <ol data-ke-list-type="decimal" start="4" style="list-style-type: decimal;">
    <li>
     완료 되면 이렇게 뜹니다. 저기 깃 표기에서 브랜치를 딸 수 있으므로 편히 작업하시길 바라겠습니다.
    </li>
   </ol>
   <p>
    <img alt="Image" src="https://github.com/user-attachments/assets/be70c397-6293-4e2f-bd20-05dae8ed28d4"/>
   </p>
   <hr data-ke-style="style1"/>
   <h3 data-ke-size="size23">
    💡 Best Practice
   </h3>
   <ul data-ke-list-type="disc" style="list-style-type: disc;">
    <li>
     여기 네 가지 아이콘 모두 각자의 역할이 있으니 확인 한 번 해보시길 바라겠습니다.
    </li>
   </ul>
   <p>
    <img alt="Image" src="https://github.com/user-attachments/assets/b7f2cf4e-51e6-46bf-9959-0140235ede95"/>
   </p>
   <hr data-ke-style="style1"/>
   <h2 data-ke-size="size26">
    3. 참고 자료
   </h2>
   <p data-ke-size="size16">
    [인텔리제이에서 jira 사용하기]
    <a href="https://velog.io/@donghune/Intelli-J-%EC%97%90%EC%84%9C-JIRA-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0">
     (https://redis.io/&amp;#41
    </a>
    ;
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
    entryId: 197
}
   </script>
   <div class="wrap_btn" data-tistory-react-app="Reaction" id="reaction-197">
   </div>
   <div class="wrap_btn wrap_btn_share">
    <button aria-expanded="false" class="btn_post sns_btn btn_share" data-blog-title="Cohe" data-description="✨ 개념 설명지라로 협업툴을 사용하게 되며브랜치 생성코드 작성PR이 순 중 브랜치 생성을 수월하게 하기 위해 아래와 같은 내용을 따라하길 권장🛠️ 사용 방법우리는 크게 2가지를 신경 쓸 것이다.JIRA에서 로그인을 위한 API 들고오기intelliJ에서 jira 연동하기1. JIRA에서 로그인을 위한 API 들고오기계정 관리를 찾아 클릭한다프로필을 찾아 계정 관리를 클릭한다그럼 아래와 같은 화면이 나오는데 보안 탭을 클릭하여 API 토큰을 클릭해봅시다그럼 이런 창이 뜨는데 API 토큰을 만들어 줍시다API 토큰을 복사하고고생 많으셨습니다 이제 인텔리제이로 넘어갑시다2. intelliJ에서 jira 연동하기jira plugin을 추가한다다운이 다 되면 아래와 같은게 뜨는데, 클릭하여 -&gt; Configur.." data-pc-url="https://code-chy.tistory.com/197" data-profile-image="https://tistory1.daumcdn.net/tistory/5646409/attach/8bf562b73e38446a9f0bb065fc30f867" data-profile-name="코헤0121" data-relative-pc-url="/197" data-thumbnail-url="https://t1.daumcdn.net/tistory_admin/static/images/openGraph/opengraph.png" data-title="intelliJ 에서 jira branch 를 쉽게 연동할 수 있도록 하는 방법" type="button">
     <span class="ico_postbtn ico_share">
      공유하기
     </span>
    </button>
    <div class="layer_post" id="tistorySnsLayer">
    </div>
   </div>
   <div class="wrap_btn wrap_btn_etc" data-category-visibility="public" data-entry-id="197" data-entry-visibility="public">
    <button aria-expanded="false" class="btn_post btn_etc2" type="button">
     <span class="ico_postbtn ico_etc">
      게시글 관리
     </span>
    </button>
    <div class="layer_post" id="tistoryEtcLayer">
    </div>
   </div>
  </div>
  <button class="btn_menu_toolbar btn_subscription #subscribe" data-blog-id="5646409" data-device="web_pc" data-tiara-action-name="구독 버튼_클릭" data-url="https://code-chy.tistory.com/197" type="button">
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
   <a href="/category/%EA%B0%9C%EB%B0%9C%20%EC%9D%B4%EB%AA%A8%EC%A0%80%EB%AA%A8">
    개발 이모저모
   </a>
   &gt;
   <a href="/category/%EA%B0%9C%EB%B0%9C%20%EC%9D%B4%EB%AA%A8%EC%A0%80%EB%AA%A8/TIL">
    TIL
   </a>
   ' 카테고리의 다른 글
  </h4>
  <table>
   <tr>
    <th>
     <a href="/143">
      Todo Controller 카테고리 별로 분류하기
     </a>
     <span>
      (0)
     </span>
    </th>
    <td>
     2024.08.16
    </td>
   </tr>
   <tr>
    <th>
     <a href="/112">
      20240614 TIL digital envelope routines::unsupported 해
     </a>
     <span>
      (0)
     </span>
    </th>
    <td>
     2024.06.14
    </td>
   </tr>
   <tr>
    <th>
     <a href="/109">
      20240419 TIL
     </a>
     <span>
      (1)
     </span>
    </th>
    <td>
     2024.04.19
    </td>
   </tr>
   <tr>
    <th>
     <a href="/66">
      the associated script can not be loaded 고치기 시작-git 버전
     </a>
     <span>
      (0)
     </span>
    </th>
    <td>
     2024.02.08
    </td>
   </tr>
   <tr>
    <th>
     <a href="/61">
      20240126 TIL
     </a>
     <span>
      (0)
     </span>
    </th>
    <td>
     2024.01.26
    </td>
   </tr>
  </table>
 </div>
 <!-- PostListinCategory - END -->
</div>
