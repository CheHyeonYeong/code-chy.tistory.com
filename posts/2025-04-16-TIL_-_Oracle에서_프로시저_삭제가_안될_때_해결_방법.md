# TIL - Oracle에서 프로시저 삭제가 안될 때 해결 방법

📅 2025-04-16

[원문 링크](https://code-chy.tistory.com/200)

---

<div class="area_view" id="article-view">
<!-- System - START -->
<div class="revenue_unit_wrap">
<div class="revenue_unit_item adfit">
<div class="revenue_unit_info">728x90</div>
<ins class="kakao_ad_area" data-ad-height="90px" data-ad-unit="DAN-nP21vcNIK4cPjSVz" data-ad-width="728px" style="display: none;"></ins>
<script async="async" src="//t1.daumcdn.net/kas/static/ba.min.js" type="text/javascript"></script>
</div>
</div>
<div class="revenue_unit_wrap">
<div class="revenue_unit_item adsense responsive">
<div class="revenue_unit_info">반응형</div>
<script async="async" src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle" data-ad-client="ca-pub-9389330875359141" data-ad-format="auto" data-ad-host="ca-host-pub-9691043933427338" style="display: block;"></ins>
<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
</div>
</div>
<!-- System - END -->
<div class="contents_style"><h1> </h1><h3 data-ke-size="size23">🗓️ 2025-04-16</h3><p data-ke-size="size16">오늘은 정말 단순하게 DROP PROCEDURE 한 줄 치면 끝날 줄 알았던 일이, 예상치 못하게 오래 걸려서 고생한 케이스를 정리해본다.<br/>결론부터 말하면 <b>세션 락</b>이 원인이었다.</p><hr data-ke-style="style1" data-ke-type="horizontalRule"/><h2 data-ke-size="size26">🧨 문제 상황</h2><ul data-ke-list-type="disc" style="list-style-type: disc;"><li>Oracle에서 기존 프로시저를 삭제하려고 DROP PROCEDURE ㅁㅁㅁㅁㅁ; 실행했는데,</li><li>쿼리는 돌고 있는데 반응이 없음.</li><li>무한 대기 상태... 심지어 에러도 안 뜸.</li></ul><hr data-ke-style="style1" data-ke-type="horizontalRule"/><h2 data-ke-size="size26">🔍 원인 분석</h2><h3 data-ke-size="size23">dba_ddl_locks로 확인해보니:</h3><pre class="sql"><code>SELECT *
FROM dba_ddl_locks
WHERE name = 'ㅁㅁㅁㅁㅁㅁㅁㅁㅁ';

</code></pre><p data-ke-size="size16">결과:</p><pre class="gherkin"><code>SESSION_ID | OWNER        | NAME              | TYPE                | MODE_HELD | MODE_REQUESTED
-----------+--------------+-------------------+---------------------+-----------+----------------
1578       | ㅁㅁㅁㅁㅁㅁㅁ| ㅁㅁㅁㅁㅁㅁㅁㅁㅁ| Table/Procedure/Type| Null      | None
488        | ㅁㅁㅁㅁㅁㅁㅁ| ㅁㅁㅁㅁㅁㅁㅁㅁㅁ| Table/Procedure/Type| Null      | None
...        | ...          | ...               | ...                 | ...       | ...

</code></pre><ul data-ke-list-type="disc" style="list-style-type: disc;"><li>여러 세션이 MODE_HELD = Null, MODE_REQUESTED = None 상태로 <b>락을 걸고 있지도 않는데도</b> 목록에 잡혀 있었다.</li><li>심지어 세션들이 좀비처럼 살아 있어서 DROP 명령이 락 대기 상태로 대기 중이었다.</li></ul><hr data-ke-style="style1" data-ke-type="horizontalRule"/><h2 data-ke-size="size26">🛠️ 해결 방법</h2><h3 data-ke-size="size23">1. 락 건 세션 목록 조회</h3><pre class="sql"><code>SELECT sid, serial#
FROM v$session
WHERE sid IN (1578, 488, 3764, 1817, 3758, 6, 1580);

</code></pre><h3 data-ke-size="size23">2. 세션 강제 종료</h3><pre class="routeros"><code>ALTER SYSTEM KILL SESSION 'SID,SERIAL#' IMMEDIATE;

</code></pre><p data-ke-size="size16">예시:</p><pre class="routeros"><code>ALTER SYSTEM KILL SESSION '1578,12345' IMMEDIATE;

</code></pre><blockquote data-ke-style="style1">
<p data-ke-size="size16">IMMEDIATE 안 붙이면 안 죽는다. 꼭 붙여야 한다.</p>
</blockquote><hr data-ke-style="style1" data-ke-type="horizontalRule"/><h3 data-ke-size="size23">✅ 그리고 다시 DROP 시도</h3><pre class="cal"><code>DROP PROCEDURE ㅁㅁㅁㅁㅁㅁㅁㅁㅁ;

</code></pre><p data-ke-size="size16">✨ 이번엔 바로 삭제 성공!</p><hr data-ke-style="style1" data-ke-type="horizontalRule"/><h2 data-ke-size="size26">💡 배운 점</h2><ul data-ke-list-type="disc" style="list-style-type: disc;"><li>Oracle은 프로시저도 DDL 객체라서 dba_ddl_locks에 잡힐 수 있다.</li><li>세션이 "현재 사용 중"이 아니더라도, 가비지 상태로 남아있으면 DDL 락이 걸려서 DROP이 안 될 수 있다.</li><li>이런 경우 v$session에서 세션 ID로 조회 → KILL SESSION으로 수동 정리 필요.</li><li>진짜 안 될 땐… 이름 바꿔서 새로 만들고 기존 건 나중에 DBA한테 지워달라고 하는 것도 방법이다 😂</li></ul><hr data-ke-style="style1" data-ke-type="horizontalRule"/><p data-ke-size="size16">📝 오늘도 하나 배웠다.<br/>Oracle이 심플한 듯 심플하지 않은 이유, 바로 이런 구석구석에서 발견된다.</p></div>
<!-- System - START -->
<div class="revenue_unit_wrap">
<div class="revenue_unit_item adfit">
<div class="revenue_unit_info">728x90</div>
<ins class="kakao_ad_area" data-ad-height="90px" data-ad-unit="DAN-Zam346sFty2LTccN" data-ad-width="728px" style="display: none;"></ins>
<script async="async" src="//t1.daumcdn.net/kas/static/ba.min.js" type="text/javascript"></script>
</div>
</div>
<div class="revenue_unit_wrap">
<div class="revenue_unit_item adsense responsive">
<div class="revenue_unit_info">반응형</div>
<script async="async" src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle" data-ad-client="ca-pub-9389330875359141" data-ad-format="auto" data-ad-host="ca-host-pub-9691043933427338" style="display: block;"></ins>
<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
</div>
</div>
<!-- System - END -->
<script async="" crossorigin="anonymous" onerror="changeAdsenseToNaverAd()" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9527582522912841"></script>
<!-- inventory -->
<ins class="adsbygoogle" data-ad-adfit-unit="DAN-HCZEy0KQLPMGnGuC" data-ad-client="ca-pub-9527582522912841" data-ad-format="auto" data-ad-slot="4947159016" data-ad-type="inventory" data-full-width-responsive="true" style="margin:50px 0; display:block"></ins>
<script id="adsense_script">
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
<script>
    if(window.ObserveAdsenseUnfilledState !== undefined){ ObserveAdsenseUnfilledState(); }
</script>
<div data-tistory-react-app="NaverAd"></div>
<div class="container_postbtn #post_button_group">
<div class="postbtn_like"><script>window.ReactionButtonType = 'reaction';
window.ReactionApiUrl = '//code-chy.tistory.com/reaction';
window.ReactionReqBody = {
    entryId: 200
}</script>
<div class="wrap_btn" data-tistory-react-app="Reaction" id="reaction-200"></div><div class="wrap_btn wrap_btn_share"><button aria-expanded="false" class="btn_post sns_btn btn_share" data-blog-title="Cohe" data-description="🗓️ 2025-04-16오늘은 정말 단순하게 DROP PROCEDURE 한 줄 치면 끝날 줄 알았던 일이, 예상치 못하게 오래 걸려서 고생한 케이스를 정리해본다.결론부터 말하면 세션 락이 원인이었다.🧨 문제 상황Oracle에서 기존 프로시저를 삭제하려고 DROP PROCEDURE ㅁㅁㅁㅁㅁ; 실행했는데,쿼리는 돌고 있는데 반응이 없음.무한 대기 상태... 심지어 에러도 안 뜸.🔍 원인 분석dba_ddl_locks로 확인해보니:SELECT *FROM dba_ddl_locksWHERE name = 'ㅁㅁㅁㅁㅁㅁㅁㅁㅁ';결과:SESSION_ID | OWNER | NAME | TYPE | MODE_HELD | MODE_REQUESTED-----.." data-pc-url="https://code-chy.tistory.com/200" data-profile-image="https://tistory1.daumcdn.net/tistory/5646409/attach/8bf562b73e38446a9f0bb065fc30f867" data-profile-name="코헤0121" data-relative-pc-url="/200" data-thumbnail-url="https://t1.daumcdn.net/tistory_admin/static/images/openGraph/opengraph.png" data-title="💻 TIL - Oracle에서 프로시저 삭제가 안될 때 해결 방법" type="button"><span class="ico_postbtn ico_share">공유하기</span></button>
<div class="layer_post" id="tistorySnsLayer"></div>
</div><div class="wrap_btn wrap_btn_etc" data-category-visibility="public" data-entry-id="200" data-entry-visibility="public"><button aria-expanded="false" class="btn_post btn_etc2" type="button"><span class="ico_postbtn ico_etc">게시글 관리</span></button>
<div class="layer_post" id="tistoryEtcLayer"></div>
</div></div>
<button class="btn_menu_toolbar btn_subscription #subscribe" data-blog-id="5646409" data-device="web_pc" data-tiara-action-name="구독 버튼_클릭" data-url="https://code-chy.tistory.com/200" type="button"><em class="txt_state"></em><strong class="txt_tool_id">Cohe</strong><span class="img_common_tistory ico_check_type1"></span></button> <div class="postbtn_ccl" data-ccl-derive="1" data-ccl-type="6">
<a class="link_ccl" href="https://creativecommons.org/licenses/by-nc/4.0/deed.ko" rel="license" target="_blank">
<span class="bundle_ccl">
<span class="ico_postbtn ico_ccl1">저작자표시</span> <span class="ico_postbtn ico_ccl2">비영리</span>
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
            --> <div data-tistory-react-app="SupportButton"></div>
</div>
<!-- PostListinCategory - START -->
<div class="another_category another_category_color_gray">
<h4>'<a href="/category/%EA%B0%9C%EB%B0%9C%20%EC%9D%B4%EB%AA%A8%EC%A0%80%EB%AA%A8">개발 이모저모</a> &gt; <a href="/category/%EA%B0%9C%EB%B0%9C%20%EC%9D%B4%EB%AA%A8%EC%A0%80%EB%AA%A8/TIL">TIL</a>' 카테고리의 다른 글</h4>
<table>
<tr>
<th><a href="/197">intelliJ 에서 jira branch 를 쉽게 연동할 수 있도록 하는 방법</a>  <span>(0)</span></th>
<td>2025.03.09</td>
</tr>
<tr>
<th><a href="/143">Todo Controller 카테고리 별로 분류하기</a>  <span>(0)</span></th>
<td>2024.08.16</td>
</tr>
<tr>
<th><a href="/112">20240614 TIL digital envelope routines::unsupported 해</a>  <span>(0)</span></th>
<td>2024.06.14</td>
</tr>
<tr>
<th><a href="/109">20240419 TIL</a>  <span>(1)</span></th>
<td>2024.04.19</td>
</tr>
<tr>
<th><a href="/66">the associated script can not be loaded 고치기 시작-git 버전</a>  <span>(0)</span></th>
<td>2024.02.08</td>
</tr>
</table>
</div>
<!-- PostListinCategory - END -->
</div>