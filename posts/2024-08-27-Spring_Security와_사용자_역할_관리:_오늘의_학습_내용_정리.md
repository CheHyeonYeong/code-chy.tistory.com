# Spring Security와 사용자 역할 관리: 오늘의 학습 내용 정리

📅 2024-08-27

[원문 링크](https://code-chy.tistory.com/148)

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
<!-- System - END -->
<div class="contents_style"><p data-ke-size="size16">오늘은 Spring Security를 사용한 사용자 인증 및 권한 관리에 대해 깊이 있게 다뤄보았습니다. 특히 사용자 역할 설정과 관련된 몇 가지 흥미로운 이슈들을 해결하면서 많은 것을 배웠습니다. 이 포스트에서는 오늘 학습한 주요 내용들을 정리해보겠습니다.</p>
<h2 data-ke-size="size26">1. 사용자 역할 확인 로직</h2>
<p data-ke-size="size16">먼저, 사용자의 역할을 확인하는 로직에 대해 알아보았습니다. Spring Security에서는 보통 다음과 같은 방식으로 역할을 확인합니다:</p>
<pre class="reasonml"><code>if (!UserRoles.BOSS.contains(loginUser.getRole())) {
    // 사용자가 BOSS 역할이 아닐 때의 로직
}</code></pre>
<p data-ke-size="size16">이 코드는 <code>UserRoles.BOSS</code>가 <code>Set&lt;Role&gt;</code> 타입이고, <code>loginUser.getRole()</code>이 사용자의 역할을 반환한다고 가정합니다.</p>
<h2 data-ke-size="size26">2. 사용자 등록(회원가입) 로직</h2>
<p data-ke-size="size16">다음으로, 사용자 등록 로직에 대해 심도 있게 살펴보았습니다. 주요 포인트는 다음과 같습니다:</p>
<ol data-ke-list-type="decimal" style="list-style-type: decimal;">
<li>이메일, 닉네임, 전화번호의 중복 체크</li>
<li>비밀번호 암호화</li>
<li>사용자 역할 설정</li>
</ol>
<p data-ke-size="size16">특히 사용자 역할 설정 부분에서 몇 가지 개선이 필요한 점을 발견했습니다:</p>
<pre class="pgsql"><code>if (userRepository.count() == 0) {
    user.addRole(UserRoles.USER);
    user.addRole(UserRoles.BOSS);
    user.addRole(UserRoles.ADMIN);
} else {
    user.addRole(UserRoles.USER);
}</code></pre>
<p data-ke-size="size16">이 로직은 첫 번째 사용자에게 모든 역할을 부여하고, 이후 사용자들에게는 USER 역할만 부여합니다.</p>
<h2 data-ke-size="size26">3. 데이터베이스 제약 조건 오류 처리</h2>
<p data-ke-size="size16">마지막으로, 데이터베이스 작업 중 발생할 수 있는 제약 조건 위반 오류에 대해 알아보았습니다. 특히 'user_role_set_chk_1' 제약 조건 위반 오류를 중점적으로 다루었습니다.</p>
<p data-ke-size="size16">이러한 오류를 방지하기 위해서는:</p>
<ol data-ke-list-type="decimal" style="list-style-type: decimal;">
<li>사용자 역할 설정 로직을 신중히 검토해야 합니다.</li>
<li>데이터베이스 스키마와 애플리케이션 로직이 일치하는지 확인해야 합니다.</li>
<li>입력 데이터의 유효성을 철저히 검사해야 합니다.</li>
</ol>
<h2 data-ke-size="size26">결론</h2>
<p data-ke-size="size16">오늘 학습을 통해 Spring Security를 사용한 사용자 인증 및 권한 관리의 복잡성과 중요성을 다시 한번 실감했습니다. 특히 사용자 역할 관리와 데이터베이스 작업 시 발생할 수 있는 오류 처리의 중요성을 깨달았습니다.</p>
<p data-ke-size="size16"> </p>
<p data-ke-size="size16">해당 pr을 보시면 작업 내용 전반을 알 수 있습니다 ^^</p>
<p data-ke-size="size16"><a href="https://github.com/ToriArtis/2NY-Backend/pull/104" rel="noopener noreferrer" target="_blank">https://github.com/ToriArtis/2NY-Backend/pull/104</a></p>
<figure contenteditable="false" data-ke-align="alignCenter" data-ke-type="opengraph" data-og-description='2NY ✨Feat: 전체 유저 보여주기 권한 부여 로직 다시 부여 전체 유저 보여주기만 지금은 가능하다 [ { "email": "user@example.com", "password": "$2a$10$FvdvEhJj30SkMIUTkHWRM.Qngfz90...' data-og-host="github.com" data-og-image="https://scrap.kakaocdn.net/dn/gsQaZ/hyWSoDIwNb/eSakMKe3InpMaB37okLF50/img.png?width=1200&amp;height=600&amp;face=0_0_1200_600" data-og-source-url="https://github.com/ToriArtis/2NY-Backend/pull/104" data-og-title="✨Feat: 전체 유저 보여주기 by CheHyeonYeong · Pull Request #104 · ToriArtis/2NY-Backend" data-og-type="object" data-og-url="https://github.com/ToriArtis/2NY-Backend/pull/104" id="og_1724745983837"><a data-source-url="https://github.com/ToriArtis/2NY-Backend/pull/104" href="https://github.com/ToriArtis/2NY-Backend/pull/104" rel="noopener" target="_blank">
<div class="og-image" style="background-image: url('https://scrap.kakaocdn.net/dn/gsQaZ/hyWSoDIwNb/eSakMKe3InpMaB37okLF50/img.png?width=1200&amp;height=600&amp;face=0_0_1200_600');"> </div>
<div class="og-text">
<p class="og-title" data-ke-size="size16">✨Feat: 전체 유저 보여주기 by CheHyeonYeong · Pull Request #104 · ToriArtis/2NY-Backend</p>
<p class="og-desc" data-ke-size="size16">2NY ✨Feat: 전체 유저 보여주기 권한 부여 로직 다시 부여 전체 유저 보여주기만 지금은 가능하다 [ { "email": "user@example.com", "password": "$2a$10$FvdvEhJj30SkMIUTkHWRM.Qngfz90...</p>
<p class="og-host" data-ke-size="size16">github.com</p>
</div>
</a></figure>
<p data-ke-size="size16"> </p>
<p data-ke-size="size16"> </p>
<p data-ke-size="size16">해피 코딩하세요! 😊</p></div>
<!-- System - START -->
<!-- System - END -->
<script async="" crossorigin="anonymous" onerror="changeAdsenseToAdfit()" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9527582522912841"></script>
<!-- inventory -->
<ins class="adsbygoogle" data-ad-adfit-unit="DAN-HCZEy0KQLPMGnGuC" data-ad-client="ca-pub-9527582522912841" data-ad-format="auto" data-ad-slot="4947159016" data-ad-type="inventory" data-full-width-responsive="true" style="margin:50px 0; display:block"></ins>
<script id="adsense_script">
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
<script>
    if(window.ObserveAdsenseUnfilledState !== undefined){ ObserveAdsenseUnfilledState(); }
</script>
<div class="container_postbtn #post_button_group">
<div class="postbtn_like"><script>window.ReactionButtonType = 'reaction';
window.ReactionApiUrl = '//code-chy.tistory.com/reaction';
window.ReactionReqBody = {
    entryId: 148
}</script>
<div class="wrap_btn" data-tistory-react-app="Reaction" id="reaction-148"></div><div class="wrap_btn wrap_btn_share"><button aria-expanded="false" class="btn_post sns_btn btn_share" data-blog-title="Cohe" data-description="오늘은 Spring Security를 사용한 사용자 인증 및 권한 관리에 대해 깊이 있게 다뤄보았습니다. 특히 사용자 역할 설정과 관련된 몇 가지 흥미로운 이슈들을 해결하면서 많은 것을 배웠습니다. 이 포스트에서는 오늘 학습한 주요 내용들을 정리해보겠습니다.1. 사용자 역할 확인 로직먼저, 사용자의 역할을 확인하는 로직에 대해 알아보았습니다. Spring Security에서는 보통 다음과 같은 방식으로 역할을 확인합니다:if (!UserRoles.BOSS.contains(loginUser.getRole())) {    // 사용자가 BOSS 역할이 아닐 때의 로직}이 코드는 UserRoles.BOSS가 Set 타입이고, loginUser.getRole()이 사용자의 역할을 반환한다고 가정합니다.2. 사용.." data-pc-url="https://code-chy.tistory.com/148" data-profile-image="https://tistory1.daumcdn.net/tistory/5646409/attach/8bf562b73e38446a9f0bb065fc30f867" data-profile-name="코헤0121" data-relative-pc-url="/148" data-thumbnail-url="https://t1.daumcdn.net/tistory_admin/static/images/openGraph/opengraph.png" data-title="Spring Security와 사용자 역할 관리: 오늘의 학습 내용 정리" type="button"><span class="ico_postbtn ico_share">공유하기</span></button>
<div class="layer_post" id="tistorySnsLayer"></div>
</div><div class="wrap_btn wrap_btn_etc" data-category-visibility="public" data-entry-id="148" data-entry-visibility="public"><button aria-expanded="false" class="btn_post btn_etc2" type="button"><span class="ico_postbtn ico_etc">게시글 관리</span></button>
<div class="layer_post" id="tistoryEtcLayer"></div>
</div></div>
<button class="btn_menu_toolbar btn_subscription #subscribe" data-blog-id="5646409" data-device="web_pc" data-tiara-action-name="구독 버튼_클릭" data-url="https://code-chy.tistory.com/148" type="button"><em class="txt_state"></em><strong class="txt_tool_id">Cohe</strong><span class="img_common_tistory ico_check_type1"></span></button> <div class="postbtn_ccl" data-ccl-derive="1" data-ccl-type="6">
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
<h4>'<a href="/category/Spring%2C%20SpringBoot">Spring, SpringBoot</a>' 카테고리의 다른 글</h4>
<table>
<tr>
<th><a href="/147">JWT를 이용한 Spring Security 인증 구현하기</a>  <span>(0)</span></th>
<td>2024.08.27</td>
</tr>
<tr>
<th><a href="/111">SpringBoot Project 게시판 만들기 2</a>  <span>(1)</span></th>
<td>2024.05.24</td>
</tr>
<tr>
<th><a href="/110">SpringBoot Project 게시판 만들기</a>  <span>(1)</span></th>
<td>2024.05.22</td>
</tr>
<tr>
<th><a href="/108">MyBatis 스프링 연동</a>  <span>(0)</span></th>
<td>2024.04.19</td>
</tr>
</table>
</div>
<!-- PostListinCategory - END -->
</div>