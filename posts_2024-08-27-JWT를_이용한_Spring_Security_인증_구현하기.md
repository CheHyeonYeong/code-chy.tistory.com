# JWT를 이용한 Spring Security 인증 구현하기

📅 2024-08-27

[원문 링크](https://code-chy.tistory.com/147)

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
   안녕하세요! 오늘은 Spring Boot 애플리케이션에서 JWT(JSON Web Token)를 사용한 인증 시스템 구현에 대해 알아보겠습니다. 특히 Access Token과 Refresh Token을 활용한 보안 강화 방법에 초점을 맞추어 설명하겠습니다.
  </p>
  <h2 data-ke-size="size26">
   1. JWT란?
  </h2>
  <p data-ke-size="size16">
   JWT는 당사자 간 정보를 안전하게 전송하기 위한 컴팩트하고 독립적인 방식의 표준입니다. 이 토큰은 디지털 서명이 되어 있어 신뢰할 수 있습니다.
  </p>
  <h2 data-ke-size="size26">
   2. TokenProvider 구현하기
  </h2>
  <p data-ke-size="size16">
   먼저, JWT 토큰을 생성하고 검증하는
   <code>
    TokenProvider
   </code>
   클래스를 구현해봅시다.
  </p>
  <pre class="reasonml"><code>
@Component
public class TokenProvider {

    // Access 토큰을 위한 암호화 키
    private final Key accessKey;
    // Refresh 토큰을 위한 암호화 키
    private final Key refreshKey;

    // 생성자: 암호화 키 초기화
    public TokenProvider() {
        // HS512 알고리즘을 사용하여 안전한 키 생성
        this.accessKey = Keys.secretKeyFor(SignatureAlgorithm.HS512);
        this.refreshKey = Keys.secretKeyFor(SignatureAlgorithm.HS512);
    }

    // Access 토큰 생성 메서드
    public String createAccessToken(User userEntity) {
        // 현재 시간으로부터 30분 후의 만료 시간 설정
        Date expiryDate = Date.from(Instant.now().plus(30, ChronoUnit.MINUTES));

        // JWT 빌더를 사용하여 토큰 생성
        return Jwts.builder()
                .setSubject(userEntity.getEmail())  // 사용자 이메일을 subject로 설정
                .setIssuer("demo app")  // 발행자 설정
                .setIssuedAt(new Date())  // 발행 시간 설정
                .setExpiration(expiryDate)  // 만료 시간 설정
                .signWith(accessKey, SignatureAlgorithm.HS512)  // 암호화 키와 알고리즘으로 서명
                .compact();  // 토큰 생성
    }

    // Refresh 토큰 생성 메서드
    public String createRefreshToken(User userEntity) {
        // 현재 시간으로부터 7일 후의 만료 시간 설정
        Date expiryDate = Date.from(Instant.now().plus(7, ChronoUnit.DAYS));

        // JWT 빌더를 사용하여 토큰 생성 (Access 토큰과 유사하지만 만료 시간이 더 김)
        return Jwts.builder()
                .setSubject(userEntity.getEmail())
                .setIssuer("demo app")
                .setIssuedAt(new Date())
                .setExpiration(expiryDate)
                .signWith(refreshKey, SignatureAlgorithm.HS512)
                .compact();
    }

    // Access 토큰 검증 및 사용자 ID 추출 메서드
    public String validateAndGetUserId(String token) {
        // 토큰을 파싱하여 Claims(페이로드) 추출
        Claims claims = Jwts.parserBuilder()
                .setSigningKey(accessKey)  // 암호화 키 설정
                .build()
                .parseClaimsJws(token)  // 토큰 파싱
                .getBody();  // Claims 얻기

        // subject(여기서는 사용자 이메일)를 반환
        return claims.getSubject();
    }

    // Refresh 토큰 검증 및 사용자 ID 추출 메서드
    public String validateAndGetUserIdFromRefreshToken(String token) {
        // Access 토큰과 유사하지만 refresh 키를 사용
        Claims claims = Jwts.parserBuilder()
                .setSigningKey(refreshKey)
                .build()
                .parseClaimsJws(token)
                .getBody();

        return claims.getSubject();
    }

    // 토큰 만료 여부 확인 메서드
    public boolean isTokenExpired(String token) {
        try {
            // 토큰에서 Claims 추출
            Claims claims = Jwts.parserBuilder()
                    .setSigningKey(accessKey)
                    .build()
                    .parseClaimsJws(token)
                    .getBody();
            // 현재 시간과 비교하여 만료 여부 반환
            return claims.getExpiration().before(new Date());
        } catch (Exception e) {
            // 예외 발생 시 만료된 것으로 간주
            return true;
        }
    }


    public long getTokenRemainingTime(String token, boolean isRefreshToken) {
        try {
            Key key = isRefreshToken ? refreshKey : accessKey;
            Claims claims = Jwts.parserBuilder()
                    .setSigningKey(key)
                    .build()
                    .parseClaimsJws(token)
                    .getBody();

            Date expiration = claims.getExpiration();
            Date now = new Date();

            return Math.max(0, expiration.getTime() - now.getTime());
        } catch (Exception e) {
            return -1; // 토큰이 유효하지 않거나 파싱 중 오류가 발생한 경우
        }
    }
}

</code></pre>
  <h2 data-ke-size="size26">
   3. JwtAuthenticationFilter 구현하기
  </h2>
  <p data-ke-size="size16">
   다음으로, 요청마다 JWT 토큰을 검증하는 필터를 구현합니다.
  </p>
  <pre class="livescript"><code>@Component
public class JwtAuthenticationFilter extends OncePerRequestFilter {
    @Autowired
    private TokenProvider tokenProvider;
   @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
        try {

            // 리퀘스트에서 토큰 가져오기.
            String accessToken = parseBearerToken(request);
            String refreshToken = request.getHeader("Refresh-Token");


            log.info("Filter is running...");
            // 토큰 검사하기. JWT이므로 인가 서버에 요청 하지 않고도 검증 가능.
            if (accessToken != null &amp;&amp; !accessToken.equalsIgnoreCase("null") &amp;&amp; StringUtils.hasText(accessToken)) {
                if(tokenProvider.isTokenExpired(refreshToken)&amp;&amp;StringUtils.hasText(refreshToken)){

                    try {
                        String email = tokenProvider.validateAndGetUserIdFromRefreshToken(refreshToken);
                        Optional&lt;User&gt; userOptional = userRepository.findByEmail(email);
                        User user = userOptional.orElseThrow(() -&gt; new BusinessLogicException(ExceptionCode.USER_NOT_FOUND));

                        // 새로운 AccessToken 생성
                        String newAccessToken = tokenProvider.createAccessToken(user);
                        response.setHeader("New-Access-Token", newAccessToken);
                        accessToken = newAccessToken;

                        // RefreshToken 만료 기간 확인 및 갱신
                        long refreshTokenRemainingTime = tokenProvider.getTokenRemainingTime(refreshToken, true);
                        if (refreshTokenRemainingTime &lt; (1000 * 60 * 60 * 24 * 3)) { // 3일 미만
                            String newRefreshToken = tokenProvider.createRefreshToken(user);
                            response.setHeader("New-Refresh-Token", newRefreshToken);
                        }
                    } catch (Exception e) {
                        log.error("Failed to refresh token", e);
                        response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "Invalid refresh token");
                        return;
                    }
                }

                // userId 가져오기. 위조 된 경우 예외 처리 된다.
                String userId = tokenProvider.validateAndGetUserId(accessToken);

                log.info("Authenticated user ID : " + userId );
                // 인증 완료; SecurityContextHolder에 등록해야 인증된 사용자라고 생각한다.
                AbstractAuthenticationToken authentication = new UsernamePasswordAuthenticationToken(
                        userId, // 인증된 사용자의 정보. 문자열이 아니어도 아무거나 넣을 수 있다.
                        null, //
                        AuthorityUtils.NO_AUTHORITIES
                );
                authentication.setDetails(new WebAuthenticationDetailsSource().buildDetails(request));
                SecurityContext securityContext = SecurityContextHolder.createEmptyContext();
                securityContext.setAuthentication(authentication);
                SecurityContextHolder.setContext(securityContext);
            }
        } catch (Exception ex) {
            logger.error("Could not set user authentication in security context", ex);
        }

        filterChain.doFilter(request, response);
    }
}</code></pre>
  <h2 data-ke-size="size26">
   4. Spring Security 설정하기
  </h2>
  <p data-ke-size="size16">
   Spring Security 설정 클래스에서 JWT 필터를 추가하고 보안 규칙을 설정합니다.
  </p>
  <pre class="less"><code>@Configuration
@Log4j2
@EnableMethodSecurity
@EnableWebSecurity
@RequiredArgsConstructor
public class SecurityConfig {

    @Autowired
    private final JwtAuthenticationFilter jwtAuthenticationFilter; // jwt 필터 의존성 주입
    private final CustomUserDetailsService userDetailsService;
    private final OAuth2Service oAuth2Service;
    private final TokenProvider tokenProvider;
    private final UserRepository userRepository;
    private final OAuth2UserService oAuth2UserService;
    private final PasswordEncoder passwordEncoder;



    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http.cors(httpSecurityCorsConfigurer -&gt; {})
                // CSRF 보호 비활성화
                .csrf(csrf -&gt; csrf.disable())

                // HTTP 요청에 대한 인가 설정
                .authorizeHttpRequests(auth -&gt; auth
                        // 나머지 모든 요청은 인증 필요
                        .requestMatchers(HttpMethod.OPTIONS, "/**").permitAll()
                        .requestMatchers("/", "/users/**", "/oauth/**").permitAll()
                        .requestMatchers("/items/info").permitAll()
                        .requestMatchers("/api/**").permitAll()
                        .requestMatchers(HttpMethod.GET, "/items/**").permitAll() // GET 요청에 대해 모든 /items/** 경로 허용
                        .requestMatchers(HttpMethod.GET, "/review/**").permitAll()
                        .anyRequest().authenticated()
                )
                // HTTP 기본 인증 비활성화
                .httpBasic(httpBasic -&gt; httpBasic.disable())
//                .oauth2Login(oauth2 -&gt; oauth2
//                        .userInfoEndpoint(userInfo -&gt; userInfo
//                                .userService(oAuth2UserService)
//                        )
//                        .successHandler(oAuth2AuthenticationSuccessHandler())
//                )
                // 세션 관리 설정을 무상태(stateless)로 설정
                .sessionManagement(session -&gt; session
                        .sessionCreationPolicy(SessionCreationPolicy.IF_REQUIRED)
                );


        // JWT 인증 필터를 CORS 필터 이후에 추가
        // jwtAuthenticationFilter에서 tokenProvider에 의존성을 주입시켜 validate 검사함
        http.addFilterAfter(jwtAuthenticationFilter, CorsFilter.class);



        http.rememberMe(rememberMe -&gt;
                rememberMe.key("123456789") // 세션에 저장해서 작업할 수 있어야 remember 되기 때문이다.
                        .rememberMeParameter("rememberMe") // 자동 로그인 체크박스의 name 속성 값
                        .tokenValiditySeconds(60 * 60 * 24 * 365) // 1년 : 60 * 60 * 24 * 365
                        .userDetailsService(userDetailsService) // 사용자 정보 서비스 설정
        );

        // 설정된 SecurityFilterChain 반환
        return http.build();
    }

    @Bean
    public AuthenticationSuccessHandler oAuth2AuthenticationSuccessHandler() {
        return new OAuth2AuthenticationSuccessHandler(tokenProvider, userRepository, passwordEncoder);
    }

}


</code></pre>
  <h2 data-ke-size="size26">
   5. Refresh Token 구현하기
  </h2>
  <p data-ke-size="size16">
   Access Token이 만료되었을 때 Refresh Token을 사용하여 새로운 Access Token을 발급받는 로직을 구현합니다.
  </p>
  <pre class="livescript"><code>
    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
        try {

            // 리퀘스트에서 토큰 가져오기.
            String accessToken = parseBearerToken(request);
            String refreshToken = request.getHeader("Refresh-Token");


            log.info("Filter is running...");
            // 토큰 검사하기. JWT이므로 인가 서버에 요청 하지 않고도 검증 가능.
            if (accessToken != null &amp;&amp; !accessToken.equalsIgnoreCase("null") &amp;&amp; StringUtils.hasText(accessToken)) {
                if(tokenProvider.isTokenExpired(refreshToken)&amp;&amp;StringUtils.hasText(refreshToken)){

                    try {
                        String email = tokenProvider.validateAndGetUserIdFromRefreshToken(refreshToken);
                        Optional&lt;User&gt; userOptional = userRepository.findByEmail(email);
                        User user = userOptional.orElseThrow(() -&gt; new BusinessLogicException(ExceptionCode.USER_NOT_FOUND));

                        // 새로운 AccessToken 생성
                        String newAccessToken = tokenProvider.createAccessToken(user);
                        response.setHeader("New-Access-Token", newAccessToken);
                        accessToken = newAccessToken;

                        // RefreshToken 만료 기간 확인 및 갱신
                        long refreshTokenRemainingTime = tokenProvider.getTokenRemainingTime(refreshToken, true);
                        if (refreshTokenRemainingTime &lt; (1000 * 60 * 60 * 24 * 3)) { // 3일 미만
                            String newRefreshToken = tokenProvider.createRefreshToken(user);
                            response.setHeader("New-Refresh-Token", newRefreshToken);
                        }
                    } catch (Exception e) {
                        log.error("Failed to refresh token", e);
                        response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "Invalid refresh token");
                        return;
                    }
                }

                // userId 가져오기. 위조 된 경우 예외 처리 된다.
                String userId = tokenProvider.validateAndGetUserId(accessToken);

                log.info("Authenticated user ID : " + userId );
                // 인증 완료; SecurityContextHolder에 등록해야 인증된 사용자라고 생각한다.
                AbstractAuthenticationToken authentication = new UsernamePasswordAuthenticationToken(
                        userId, // 인증된 사용자의 정보. 문자열이 아니어도 아무거나 넣을 수 있다.
                        null, //
                        AuthorityUtils.NO_AUTHORITIES
                );
                authentication.setDetails(new WebAuthenticationDetailsSource().buildDetails(request));
                SecurityContext securityContext = SecurityContextHolder.createEmptyContext();
                securityContext.setAuthentication(authentication);
                SecurityContextHolder.setContext(securityContext);
            }
        } catch (Exception ex) {
            logger.error("Could not set user authentication in security context", ex);
        }

        filterChain.doFilter(request, response);
    }</code></pre>
  <h2 data-ke-size="size26">
   마무리
  </h2>
  <p data-ke-size="size16">
   이렇게 JWT를 이용한 인증 시스템을 Spring Boot 애플리케이션에 구현해보았습니다. 이 방식은 서버의 상태를 저장하지 않는 (stateless) 인증 방식으로, 확장성이 뛰어나고 보안성도 높습니다.
  </p>
  <p data-ke-size="size16">
   해당 코드 전체가 필요하시다면 깃허브를 방문해주세요~!
  </p>
  <p data-ke-size="size16">
   <a href="https://github.com/ToriArtis/2NY-Backend" rel="noopener noreferrer" target="_blank">
    https://github.com/ToriArtis/2NY-Backend
   </a>
  </p>
 </div>
 <!-- System - START -->
 <!-- System - END -->
 <div class="container_postbtn #post_button_group">
  <div class="postbtn_like">
   <script>
    window.ReactionButtonType = 'reaction';
window.ReactionApiUrl = '//code-chy.tistory.com/reaction';
window.ReactionReqBody = {
    entryId: 147
}
   </script>
   <div class="wrap_btn" data-tistory-react-app="Reaction" id="reaction-147">
   </div>
   <div class="wrap_btn wrap_btn_share">
    <button aria-expanded="false" class="btn_post sns_btn btn_share" data-blog-title="Cohe" data-description="안녕하세요! 오늘은 Spring Boot 애플리케이션에서 JWT(JSON Web Token)를 사용한 인증 시스템 구현에 대해 알아보겠습니다. 특히 Access Token과 Refresh Token을 활용한 보안 강화 방법에 초점을 맞추어 설명하겠습니다.1. JWT란?JWT는 당사자 간 정보를 안전하게 전송하기 위한 컴팩트하고 독립적인 방식의 표준입니다. 이 토큰은 디지털 서명이 되어 있어 신뢰할 수 있습니다.2. TokenProvider 구현하기먼저, JWT 토큰을 생성하고 검증하는 TokenProvider 클래스를 구현해봅시다.@Componentpublic class TokenProvider {    // Access 토큰을 위한 암호화 키    private final Key accessKey;  .." data-pc-url="https://code-chy.tistory.com/147" data-profile-image="https://tistory1.daumcdn.net/tistory/5646409/attach/8bf562b73e38446a9f0bb065fc30f867" data-profile-name="코헤0121" data-relative-pc-url="/147" data-thumbnail-url="https://t1.daumcdn.net/tistory_admin/static/images/openGraph/opengraph.png" data-title="JWT를 이용한 Spring Security 인증 구현하기" type="button">
     <span class="ico_postbtn ico_share">
      공유하기
     </span>
    </button>
    <div class="layer_post" id="tistorySnsLayer">
    </div>
   </div>
   <div class="wrap_btn wrap_btn_etc" data-category-visibility="public" data-entry-id="147" data-entry-visibility="public">
    <button aria-expanded="false" class="btn_post btn_etc2" type="button">
     <span class="ico_postbtn ico_etc">
      게시글 관리
     </span>
    </button>
    <div class="layer_post" id="tistoryEtcLayer">
    </div>
   </div>
  </div>
  <button class="btn_menu_toolbar btn_subscription #subscribe" data-blog-id="5646409" data-device="web_pc" data-tiara-action-name="구독 버튼_클릭" data-url="https://code-chy.tistory.com/147" type="button">
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
   <a href="/category/Spring%2C%20SpringBoot">
    Spring, SpringBoot
   </a>
   ' 카테고리의 다른 글
  </h4>
  <table>
   <tr>
    <th>
     <a href="/148">
      Spring Security와 사용자 역할 관리: 오늘의 학습 내용 정리
     </a>
     <span>
      (0)
     </span>
    </th>
    <td>
     2024.08.27
    </td>
   </tr>
   <tr>
    <th>
     <a href="/111">
      SpringBoot Project 게시판 만들기 2
     </a>
     <span>
      (1)
     </span>
    </th>
    <td>
     2024.05.24
    </td>
   </tr>
   <tr>
    <th>
     <a href="/110">
      SpringBoot Project 게시판 만들기
     </a>
     <span>
      (1)
     </span>
    </th>
    <td>
     2024.05.22
    </td>
   </tr>
   <tr>
    <th>
     <a href="/108">
      MyBatis 스프링 연동
     </a>
     <span>
      (0)
     </span>
    </th>
    <td>
     2024.04.19
    </td>
   </tr>
  </table>
 </div>
 <!-- PostListinCategory - END -->
</div>
