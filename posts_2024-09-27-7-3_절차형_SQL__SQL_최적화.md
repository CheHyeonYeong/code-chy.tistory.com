# 7-3 절차형 SQL/ SQL 최적화

📅 2024-09-27

[원문 링크](https://code-chy.tistory.com/163)

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
  <h1>
   절차형 SQL
  </h1>
  <ol data-ke-list-type="decimal" style="list-style-type: decimal;">
   <li>
    절차형 SQL(Procedural SQL)의 개념
    <ul data-ke-list-type="disc" style="list-style-type: disc;">
     <li>
      <b>
       SQL 언어에서도 절차 지향적인 프로그램이 가능하도록 하는 트랜잭션 언어
      </b>
     </li>
    </ul>
   </li>
   <li>
    절차형 SQL의 종류
    <ul data-ke-list-type="disc" style="list-style-type: disc;">
     <li>
      프로시저, 사용자 정의 함수, 트리거가 있다.
     </li>
    </ul>
   </li>
  </ol>
  <table data-ke-align="alignLeft" style="height: 118px;">
   <thead>
    <tr style="height: 21px;">
     <th style="height: 21px; width: 184px;">
      종류
     </th>
     <th style="height: 21px; width: 670px;">
      설명
     </th>
    </tr>
   </thead>
   <tbody>
    <tr style="height: 20px;">
     <td style="height: 20px; width: 184px;">
      <b>
       프로시저(Procedure)
      </b>
     </td>
     <td style="height: 20px; width: 670px;">
      일련의 쿼리들을 마치 하나의 함수처럼 실행하기 위한 쿼리의 집합
     </td>
    </tr>
    <tr style="height: 37px;">
     <td style="height: 37px; width: 184px;">
      <b>
       사용자 정의 함수
       <br/>
       (User-Defined Function)
      </b>
     </td>
     <td style="height: 37px; width: 670px;">
      특정 작업을 수행하는 사용자가 정의한 함수입니다.
     </td>
    </tr>
    <tr style="height: 40px;">
     <td style="height: 40px; width: 184px;">
      <b>
       트리거(Trigger)
      </b>
     </td>
     <td style="height: 40px; width: 670px;">
      데이터베이스 시스템에 삽입, 갱신, 삭제 등의
      <b>
       이벤트가 발생
      </b>
      할 때마다
      <b>
       관련 작업이 자동으로 수행되는 절차형 SQL
      </b>
     </td>
    </tr>
   </tbody>
  </table>
  <h1>
   SQL 최적화
  </h1>
  <h2 data-ke-size="size26">
   1. 쿼리 성능 개선(튜닝)의 개념
  </h2>
  <ul data-ke-list-type="disc" style="list-style-type: disc;">
   <li>
    쿼리 성능 개선 : 프로시저에 있는 SQL 실행 계획을 분석, 수정을 통해 최소의 시간으로 원하는 결과를 얻도록 프로시저를 수정하는 작업
   </li>
   <li>
    SQL 성능 개선을 통해 데이터 조작 프로시저의 성능이 가능하다.2. 쿼리 성능 개선 절차
   </li>
  </ul>
  <table data-ke-align="alignLeft" style="height: 241px;">
   <thead>
    <tr style="height: 21px;">
     <th style="width: 32px; height: 21px;">
      순서
     </th>
     <th style="width: 155px; height: 21px;">
      절차
     </th>
     <th style="width: 665px; height: 21px;">
      설명
     </th>
    </tr>
   </thead>
   <tbody>
    <tr style="height: 40px;">
     <td style="width: 32px; height: 40px;">
      1
     </td>
     <td style="width: 155px; height: 40px;">
      <b>
       문제 있는 SQL 식별
      </b>
     </td>
     <td style="width: 665px; height: 40px;">
      • 문제 있는 SQL을 식별하기 위해 애플리케이션의 성능을 관리 및 모니터링 도구인 APM 등을 활용
     </td>
    </tr>
    <tr style="height: 40px;">
     <td style="width: 32px; height: 40px;">
      2
     </td>
     <td style="width: 155px; height: 40px;">
      <b>
       옵티마이저 통계 확인
      </b>
     </td>
     <td style="width: 665px; height: 40px;">
      • 옵티마이저는 개발자가 작성한 SQL을 가장 빠르고 효율적으로 수행할 최적의 처리경로를 생성해주는 데이터베이스 핵심모듈
     </td>
    </tr>
    <tr style="height: 60px;">
     <td style="width: 32px; height: 60px;">
      3
     </td>
     <td style="width: 155px; height: 60px;">
      <b>
       SQL 문 재구성
      </b>
     </td>
     <td style="width: 665px; height: 60px;">
      - 범위가 아닌 특정 값 지정으로 범위를 줄여 처리속도를 빠르게 함
      <br/>
      • 옵티마이저가 비정상적인 실행계획을 수립할 경우, 힌트(Hint)로서 옵티마이저의 접근 경로 및 조인(Join) 순서를 제어
     </td>
    </tr>
    <tr style="height: 40px;">
     <td style="width: 32px; height: 40px;">
      4
     </td>
     <td style="width: 155px; height: 40px;">
      <b>
       인덱스 재구성
      </b>
     </td>
     <td style="width: 665px; height: 40px;">
      • 성능에 중요한 액세스 경로를 고려하여 인덱스(Index) 생성
      <br/>
      • 실행계획을 검토하여 기존 인덱스의 열 순서를 변경/추가
     </td>
    </tr>
    <tr style="height: 40px;">
     <td style="width: 32px; height: 40px;">
      5
     </td>
     <td style="width: 155px; height: 40px;">
      <b>
       실행계획 유지관리
      </b>
     </td>
     <td style="width: 665px; height: 40px;">
      데이터베이스 버전 업그레이드, 데이터 전환 등 시스템 환경의 변경 사항 발생 시에도 실행계획이 유지되고 있는지 관리
     </td>
    </tr>
   </tbody>
  </table>
  <h2 data-ke-size="size26">
   3. 옵티마이저 통계 확인
  </h2>
  <ol data-ke-list-type="decimal" style="list-style-type: decimal;">
   <li>
    옵티마이저의 개념
    <ul data-ke-list-type="disc" style="list-style-type: disc;">
     <li>
      옵티마이저는 SQL을 가장 빠르고 효율적으로 수행할 최적의 처리경로를 생성해주는
      <b>
       DBMS 내부의 핵심엔진
      </b>
      이다.
     </li>
     <li>
      옵티마이저가 생성한 SQL 처리경로를 실행계획(Execution Plan)이라고 부른다.
     </li>
    </ul>
   </li>
   <li>
    옵티마이저의 유형
    <ul data-ke-list-type="disc" style="list-style-type: disc;">
     <li>
      옵티마이저의 유형으로는 RBO(Rule Based Optimizer)와 CBO(Cost Based Optimizer)가 있다
     </li>
    </ul>
   </li>
  </ol>
  <table data-ke-align="alignLeft">
   <thead>
    <tr>
     <th>
      항목
     </th>
     <th>
      규칙기반 옵티마이저
     </th>
     <th>
      비용기반 옵티마이저
     </th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>
      개념
     </td>
     <td>
      통계 정보가 없는 상태에서 사전 등록된 규칙에 따라 질의 실행 계획을 선택하는 옵티마이저
     </td>
     <td>
      통계 정보로부터 모든 접근 경로를 고려한 질의 실행 계획을 선택하는 옵티마이저
     </td>
    </tr>
    <tr>
     <td>
      핵심
     </td>
     <td>
      규칙(우선순위) 기반
     </td>
     <td>
      비용(수행 시간) 기반
     </td>
    </tr>
    <tr>
     <td>
      평가기준
     </td>
     <td>
      인덱스 구조, 연산자, 조건절 형태
     </td>
     <td>
      코드 개수, 블록 개수, 평균 행 길이, 컬럼 값의 수, 컬럼 값 분포, 인덱스 높이, 클러스터링 팩터 등
     </td>
    </tr>
    <tr>
     <td>
      장점
     </td>
     <td>
      사용자가 원하는 처리경로로 유도하기가 쉬움
     </td>
     <td>
      옵티마이저의 이해도가 낮아도 성능 보장 가능 (기본 설정)
     </td>
    </tr>
   </tbody>
  </table>
 </div>
 <!-- System - START -->
 <!-- System - END -->
 <div class="container_postbtn #post_button_group">
  <div class="postbtn_like">
   <script>
    window.ReactionButtonType = 'reaction';
window.ReactionApiUrl = '//code-chy.tistory.com/reaction';
window.ReactionReqBody = {
    entryId: 163
}
   </script>
   <div class="wrap_btn" data-tistory-react-app="Reaction" id="reaction-163">
   </div>
   <div class="wrap_btn wrap_btn_share">
    <button aria-expanded="false" class="btn_post sns_btn btn_share" data-blog-title="Cohe" data-description="절차형 SQL절차형 SQL(Procedural SQL)의 개념SQL 언어에서도 절차 지향적인 프로그램이 가능하도록 하는 트랜잭션 언어절차형 SQL의 종류프로시저, 사용자 정의 함수, 트리거가 있다.종류설명프로시저(Procedure)일련의 쿼리들을 마치 하나의 함수처럼 실행하기 위한 쿼리의 집합사용자 정의 함수 (User-Defined Function)특정 작업을 수행하는 사용자가 정의한 함수입니다.트리거(Trigger)데이터베이스 시스템에 삽입, 갱신, 삭제 등의 이벤트가 발생할 때마다 관련 작업이 자동으로 수행되는 절차형 SQLSQL 최적화1. 쿼리 성능 개선(튜닝)의 개념쿼리 성능 개선 : 프로시저에 있는 SQL 실행 계획을 분석, 수정을 통해 최소의 시간으로 원하는 결과를 얻도록 프로시저를 수정하는.." data-pc-url="https://code-chy.tistory.com/163" data-profile-image="https://tistory1.daumcdn.net/tistory/5646409/attach/8bf562b73e38446a9f0bb065fc30f867" data-profile-name="코헤0121" data-relative-pc-url="/163" data-thumbnail-url="https://t1.daumcdn.net/tistory_admin/static/images/openGraph/opengraph.png" data-title="7-3 절차형 SQL/ SQL 최적화" type="button">
     <span class="ico_postbtn ico_share">
      공유하기
     </span>
    </button>
    <div class="layer_post" id="tistorySnsLayer">
    </div>
   </div>
   <div class="wrap_btn wrap_btn_etc" data-category-visibility="public" data-entry-id="163" data-entry-visibility="public">
    <button aria-expanded="false" class="btn_post btn_etc2" type="button">
     <span class="ico_postbtn ico_etc">
      게시글 관리
     </span>
    </button>
    <div class="layer_post" id="tistoryEtcLayer">
    </div>
   </div>
  </div>
  <button class="btn_menu_toolbar btn_subscription #subscribe" data-blog-id="5646409" data-device="web_pc" data-tiara-action-name="구독 버튼_클릭" data-url="https://code-chy.tistory.com/163" type="button">
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
 <!-- PostListinCategory - END -->
</div>
