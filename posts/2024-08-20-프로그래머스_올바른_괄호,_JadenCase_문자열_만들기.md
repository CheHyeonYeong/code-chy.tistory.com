# 프로그래머스 올바른 괄호, JadenCase 문자열 만들기

📅 2024-08-20

[원문 링크](https://code-chy.tistory.com/145)

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
   올바른 괄호
  </h1>
  <h2 data-ke-size="size26">
   문제
  </h2>
  <pre class="kotlin"><code>
문제 설명
괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

제한사항
문자열 s의 길이 : 100,000 이하의 자연수
문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.
</code></pre>
  <h2 data-ke-size="size26">
   풀이
  </h2>
  <ul data-ke-list-type="disc" style="list-style-type: disc;">
   <li>
    스택으로 풀어야 한다..
   </li>
   <li>
    나 스택은 아는데 왜 못풀었지ㅠㅠ
   </li>
  </ul>
  <pre class="gradle"><code>def solution(s):
    stack = []
    for char in s : 
        if char =='(':
            stack.append(char)
        elif char == ')':
            if not stack : 
                return False
            stack.pop()
    return len(stack) == 0</code></pre>
  <h1>
   JadenCase 문자열 만들기
  </h1>
  <h2 data-ke-size="size26">
   문제
  </h2>
  <pre class="erlang"><code>문제 설명
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

제한 조건
s는 길이 1 이상 200 이하인 문자열입니다.
s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.
숫자는 단어의 첫 문자로만 나옵니다.
숫자로만 이루어진 단어는 없습니다.
공백문자가 연속해서 나올 수 있습니다.</code></pre>
  <h3 data-ke-size="size23">
   고민
  </h3>
  <ul data-ke-list-type="disc" style="list-style-type: disc;">
   <li>
    일단 split으로 해결하고 싶었는데 잘 안됐다.. 띄어쓰기가 다 지워져서 너무 속상하다..
    <br/>
    -&gt; 이 부분 찾아보니까 내가 잘못안 부분이었다! 인공지능을 써보니
    <br/>
    <code>
     s.split() 대신 s.split(' ')를 사용하여 연속된 공백을 유지합니다.
    </code>
    이렇게 나왔다
   </li>
  </ul>
  <h2 data-ke-size="size26">
   풀이
  </h2>
  <pre class="livecodeserver"><code>
def solution(s):
    # 문자열을 공백을 기준으로 나누되, 연속된 공백도 유지
    words = s.split(' ')

    jaden_words = []
    for word in words:
        if word:
            # 첫 글자를 대문자로, 나머지는 소문자로 변환
            jaden_word = word[0].upper() + word[1:].lower()
            jaden_words.append(jaden_word)
        else:
            # 빈 문자열(연속된 공백)은 그대로 추가
            jaden_words.append(word)

    # 변환된 단어들을 다시 공백으로 연결
    return ' '.join(jaden_words)

</code></pre>
 </div>
 <!-- System - START -->
 <!-- System - END -->
 <div class="container_postbtn #post_button_group">
  <div class="postbtn_like">
   <script>
    window.ReactionButtonType = 'reaction';
window.ReactionApiUrl = '//code-chy.tistory.com/reaction';
window.ReactionReqBody = {
    entryId: 145
}
   </script>
   <div class="wrap_btn" data-tistory-react-app="Reaction" id="reaction-145">
   </div>
   <div class="wrap_btn wrap_btn_share">
    <button aria-expanded="false" class="btn_post sns_btn btn_share" data-blog-title="Cohe" data-description="올바른 괄호문제문제 설명괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어&quot;()()&quot; 또는 &quot;(())()&quot; 는 올바른 괄호입니다.&quot;)()(&quot; 또는 &quot;(()(&quot; 는 올바르지 않은 괄호입니다.'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.제한사항문자열 s의 길이 : 100,000 이하의 자연수문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.풀이스택으로 풀어야 한다..나 스택은 아는데 왜 못풀었지ㅠㅠdef solution(s):    stack = []    for cha.." data-pc-url="https://code-chy.tistory.com/145" data-profile-image="https://tistory1.daumcdn.net/tistory/5646409/attach/8bf562b73e38446a9f0bb065fc30f867" data-profile-name="코헤0121" data-relative-pc-url="/145" data-thumbnail-url="https://t1.daumcdn.net/tistory_admin/static/images/openGraph/opengraph.png" data-title="프로그래머스 올바른 괄호, JadenCase 문자열 만들기" type="button">
     <span class="ico_postbtn ico_share">
      공유하기
     </span>
    </button>
    <div class="layer_post" id="tistorySnsLayer">
    </div>
   </div>
   <div class="wrap_btn wrap_btn_etc" data-category-visibility="public" data-entry-id="145" data-entry-visibility="public">
    <button aria-expanded="false" class="btn_post btn_etc2" type="button">
     <span class="ico_postbtn ico_etc">
      게시글 관리
     </span>
    </button>
    <div class="layer_post" id="tistoryEtcLayer">
    </div>
   </div>
  </div>
  <button class="btn_menu_toolbar btn_subscription #subscribe" data-blog-id="5646409" data-device="web_pc" data-tiara-action-name="구독 버튼_클릭" data-url="https://code-chy.tistory.com/145" type="button">
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
   <a href="/category/%EA%B0%9C%EB%B0%9C%20%EC%9D%B4%EB%AA%A8%EC%A0%80%EB%AA%A8/%EC%BD%94%EB%94%A9%20%ED%85%8C%EC%8A%A4%ED%8A%B8%20%EA%B3%B5%EB%B6%80">
    코딩 테스트 공부
   </a>
   ' 카테고리의 다른 글
  </h4>
  <table>
   <tr>
    <th>
     <a href="/168">
      프로그래머스 명예의 전당
     </a>
     <span>
      (1)
     </span>
    </th>
    <td>
     2024.10.01
    </td>
   </tr>
   <tr>
    <th>
     <a href="/164">
      프로그래머스 최소직사각형
     </a>
     <span>
      (2)
     </span>
    </th>
    <td>
     2024.09.28
    </td>
   </tr>
   <tr>
    <th>
     <a href="/88">
      기능개발
     </a>
     <span>
      (0)
     </span>
    </th>
    <td>
     2024.03.29
    </td>
   </tr>
  </table>
 </div>
 <!-- PostListinCategory - END -->
</div>
