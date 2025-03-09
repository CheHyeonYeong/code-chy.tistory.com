# du/df, mkfs, 파티션 ID, fsck

📅 2024-11-12

[원문 링크](https://code-chy.tistory.com/183)

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
  <h2>
   1. 디스크 사용량 확인 명령어
  </h2>
  <h3>
   du (Disk Usage)
  </h3>
  <ul>
   <li>
    특정 디렉토리를 기준으로 디스크 사용량을 확인하는 명령어
   </li>
   <li>
    주요 옵션:
    <ul>
     <li>
      <code>
       -h
      </code>
      : 사람이 읽기 쉬운 형태로 출력 (MB, GB 등)
     </li>
     <li>
      <code>
       -s
      </code>
      : 총 사용량만 표시
     </li>
     <li>
      <code>
       --max-depth=N
      </code>
      : 특정 깊이까지만 표시
     </li>
    </ul>
   </li>
  </ul>
  <pre><code class="language-bash"># 현재 디렉토리의 용량 확인
du -h

# 특정 디렉토리의 전체 용량만 확인
du -sh /home</code></pre>
  <h3>
   df (Disk Free)
  </h3>
  <ul>
   <li>
    시스템 전체의 디스크 공간을 확인하는 명령어
   </li>
   <li>
    마운트된 모든 파일시스템의 사용량 표시
   </li>
   <li>
    주요 옵션:
    <ul>
     <li>
      <code>
       -h
      </code>
      : 사람이 읽기 쉬운 형태로 출력
     </li>
     <li>
      <code>
       -T
      </code>
      : 파일시스템 종류도 함께 표시
     </li>
    </ul>
   </li>
  </ul>
  <pre><code class="language-bash"># 전체 디스크 사용량 확인
df -h

# 파일시스템 종류와 함께 확인
df -hT</code></pre>
  <h2>
   2. 파일시스템 생성 (mkfs)
  </h2>
  <h3>
   mkfs 개요
  </h3>
  <ul>
   <li>
    make filesystem의 약자
   </li>
   <li>
    새로운 파일시스템을 생성하는 명령어
   </li>
   <li>
    다양한 파일시스템 지원
   </li>
  </ul>
  <h3>
   파일시스템 별 생성 방법
  </h3>
  <h4>
   ext2 파일시스템
  </h4>
  <pre><code class="language-bash">mke2fs /dev/장치명</code></pre>
  <h4>
   ext3 파일시스템
  </h4>
  <pre><code class="language-bash"># 방법 1
mke2fs -j /dev/장치명

# 방법 2
mke2fs -t ext3 /dev/장치명</code></pre>
  <h4>
   ext4 파일시스템
  </h4>
  <pre><code class="language-bash">mke2fs -t ext4 /dev/장치명</code></pre>
  <h3>
   주요 옵션
  </h3>
  <ul>
   <li>
    <code>
     -i
    </code>
    : i-node 개수 설정
   </li>
   <li>
    <code>
     -T
    </code>
    : i-node 크기 설정
   </li>
   <li>
    <code>
     -j
    </code>
    : 저널링 파일시스템 설정 (ext3에서 사용)
   </li>
  </ul>
  <blockquote data-ke-style="style1">
   <p data-ke-size="size16">
    <span style="font-family: 'Noto Serif KR';">
     <p>
      <strong>
       참고
      </strong>
      : ext3와 ext4의 주요 차이점
     </p>
     <ul>
      <li>
       ext3는 최초로 저널링 기능이 도입된 파일시스템
      </li>
      <li>
       ext4는 기본적으로 저널링이 포함되어 있어
       <code>
        -j
       </code>
       옵션이 불필요
      </li>
      <li>
       ext4는 ext3보다 향상된 성능과 더 큰 파일시스템 지원
      </li>
     </ul>
    </span>
   </p>
  </blockquote>
  <h2>
   3. 파일시스템 검사 및 복구 (fsck)
  </h2>
  <h3>
   fsck 개요
  </h3>
  <ul>
   <li>
    파일시스템을 검사하고 손상된 부분을 복구하는 도구
   </li>
   <li>
    e2fsck는 fsck의 확장판이지만 실질적으로 동일한 기능 제공
   </li>
  </ul>
  <h3>
   주요 특징
  </h3>
  <ul>
   <li>
    부팅 시 자동으로 실행되어 파일시스템 점검
   </li>
   <li>
    <code>
     /lost+found
    </code>
    디렉토리에서 복구 작업 수행
    <ul>
     <li>
      손상된 파일이나 디렉토리 복구 시 이 곳에 임시 저장
     </li>
     <li>
      각 파일시스템마다 독립적인
      <code>
       /lost+found
      </code>
      디렉토리 존재
     </li>
    </ul>
   </li>
  </ul>
  <pre><code class="language-bash"># 기본적인 파일시스템 검사
fsck /dev/장치명

# 강제로 검사 수행
fsck -f /dev/장치명</code></pre>
  <h2>
   4. 리눅스 파티션 ID 정리
  </h2>
  <p>
   리눅스 시스템에서 파티션의 종류를 구분하는 ID 값들을 알아보겠습니다. 이 값들은
   <code>
    fdisk
   </code>
   명령어로 파티션 작업을 할 때 특히 중요합니다.
  </p>
  <h3>
   주요 파티션 ID 목록
  </h3>
  <h4>
   기본 파티션 타입
  </h4>
  <ul>
   <li>
    <code>
     0
    </code>
    : Empty (비어있음)
   </li>
   <li>
    <code>
     1
    </code>
    : FAT12 (DOS 12-bit FAT)
   </li>
   <li>
    <code>
     4
    </code>
    : FAT16 (16-bit FAT &lt; 32M)
   </li>
   <li>
    <code>
     5
    </code>
    : Extended (확장 파티션)
   </li>
   <li>
    <code>
     6
    </code>
    : FAT16 (16-bit FAT &gt;= 32M)
   </li>
  </ul>
  <h4>
   리눅스 관련 파티션
  </h4>
  <ul>
   <li>
    <code>
     82
    </code>
    : Linux swap (스왑 파티션)
   </li>
   <li>
    <code>
     83
    </code>
    : Linux (기본 리눅스 파티션)
   </li>
   <li>
    <code>
     85
    </code>
    : Linux extended (리눅스 확장 파티션)
   </li>
   <li>
    <code>
     8e
    </code>
    : Linux LVM (논리 볼륨 관리)
   </li>
   <li>
    <code>
     fd
    </code>
    : Linux RAID auto (자동 RAID)
   </li>
  </ul>
  <h4>
   NTFS/Windows 관련
  </h4>
  <ul>
   <li>
    <code>
     7
    </code>
    : NTFS/HPFS
   </li>
   <li>
    <code>
     27
    </code>
    : Hidden NTFS Windows
   </li>
   <li>
    <code>
     3c
    </code>
    : PartitionMagic
   </li>
   <li>
    <code>
     86
    </code>
    : NTFS volume set
   </li>
   <li>
    <code>
     87
    </code>
    : NTFS volume set
   </li>
  </ul>
  <h4>
   기타 시스템 파티션
  </h4>
  <ul>
   <li>
    <code>
     a5
    </code>
    : FreeBSD
   </li>
   <li>
    <code>
     a6
    </code>
    : OpenBSD
   </li>
   <li>
    <code>
     a7
    </code>
    : NeXTSTEP
   </li>
   <li>
    <code>
     a8
    </code>
    : Darwin UFS
   </li>
   <li>
    <code>
     a9
    </code>
    : NetBSD
   </li>
   <li>
    <code>
     ab
    </code>
    : Darwin boot
   </li>
   <li>
    <code>
     be
    </code>
    : Solaris boot
   </li>
  </ul>
  <h3>
   파티션 ID 확인 방법
  </h3>
  <pre><code class="language-bash"># 전체 파티션 정보 확인
fdisk -l

# 특정 디바이스의 파티션 정보 확인
fdisk -l /dev/sda</code></pre>
  <h3>
   주요 파티션 ID 사용 예시
  </h3>
  <ol>
   <li>
    <p>
     <strong>
      리눅스 기본 설치 시
     </strong>
    </p>
    <ul>
     <li>
      루트 파티션 (
      <code>
       /
      </code>
      ):
      <code>
       83
      </code>
      (Linux)
     </li>
     <li>
      스왑 파티션:
      <code>
       82
      </code>
      (Linux swap)
     </li>
     <li>
      필요시 확장 파티션:
      <code>
       5
      </code>
      (Extended)
     </li>
    </ul>
   </li>
   <li>
    <p>
     <strong>
      LVM 구성 시
     </strong>
    </p>
    <ul>
     <li>
      LVM 파티션:
      <code>
       8e
      </code>
      (Linux LVM)
     </li>
    </ul>
   </li>
   <li>
    <p>
     <strong>
      RAID 구성 시
     </strong>
    </p>
    <ul>
     <li>
      RAID 파티션:
      <code>
       fd
      </code>
      (Linux RAID auto)
     </li>
    </ul>
   </li>
  </ol>
  <h3>
   파티션 ID 변경 방법
  </h3>
  <p>
   fdisk에서 파티션 ID를 변경하는 절차:
  </p>
  <pre><code class="language-bash"># 1. fdisk 실행
fdisk /dev/sda

# 2. 't' 명령어로 파티션 타입 변경 모드 진입
Command (m for help): t

# 3. 파티션 번호 선택
Partition number (1-4): 1

# 4. 새로운 파티션 ID 입력
Hex code (type L to list all codes): 83

# 5. 'w' 명령어로 변경사항 저장
Command (m for help): w</code></pre>
  <blockquote data-ke-style="style1">
   <p data-ke-size="size16">
    <span style="font-family: 'Noto Serif KR';">
     <p>
      <strong>
       주의사항
      </strong>
      :
     </p>
     <ul>
      <li>
       파티션 ID 변경은 데이터 손실 위험이 있으므로 백업 후 진행
      </li>
      <li>
       시스템 파티션의 ID 변경은 부팅 불가 상태를 초래할 수 있음
      </li>
      <li>
       변경 전 반드시 해당 파티션이 마운트되어 있지 않은지 확인
      </li>
     </ul>
    </span>
   </p>
  </blockquote>
 </div>
 <!-- System - START -->
 <!-- System - END -->
 <div class="container_postbtn #post_button_group">
  <div class="postbtn_like">
   <script>
    window.ReactionButtonType = 'reaction';
window.ReactionApiUrl = '//code-chy.tistory.com/reaction';
window.ReactionReqBody = {
    entryId: 183
}
   </script>
   <div class="wrap_btn" data-tistory-react-app="Reaction" id="reaction-183">
   </div>
   <div class="wrap_btn wrap_btn_share">
    <button aria-expanded="false" class="btn_post sns_btn btn_share" data-blog-title="Cohe" data-description="1. 디스크 사용량 확인 명령어du (Disk Usage)특정 디렉토리를 기준으로 디스크 사용량을 확인하는 명령어주요 옵션:-h: 사람이 읽기 쉬운 형태로 출력 (MB, GB 등)-s: 총 사용량만 표시--max-depth=N: 특정 깊이까지만 표시# 현재 디렉토리의 용량 확인du -h# 특정 디렉토리의 전체 용량만 확인du -sh /homedf (Disk Free)시스템 전체의 디스크 공간을 확인하는 명령어마운트된 모든 파일시스템의 사용량 표시주요 옵션:-h: 사람이 읽기 쉬운 형태로 출력-T: 파일시스템 종류도 함께 표시# 전체 디스크 사용량 확인df -h# 파일시스템 종류와 함께 확인df -hT2. 파일시스템 생성 (mkfs)mkfs 개요make filesystem의 약자새로운 파일시스템을 생성하는.." data-pc-url="https://code-chy.tistory.com/183" data-profile-image="https://tistory1.daumcdn.net/tistory/5646409/attach/8bf562b73e38446a9f0bb065fc30f867" data-profile-name="코헤0121" data-relative-pc-url="/183" data-thumbnail-url="https://t1.daumcdn.net/tistory_admin/static/images/openGraph/opengraph.png" data-title="du/df, mkfs, 파티션 ID, fsck" type="button">
     <span class="ico_postbtn ico_share">
      공유하기
     </span>
    </button>
    <div class="layer_post" id="tistorySnsLayer">
    </div>
   </div>
   <div class="wrap_btn wrap_btn_etc" data-category-visibility="public" data-entry-id="183" data-entry-visibility="public">
    <button aria-expanded="false" class="btn_post btn_etc2" type="button">
     <span class="ico_postbtn ico_etc">
      게시글 관리
     </span>
    </button>
    <div class="layer_post" id="tistoryEtcLayer">
    </div>
   </div>
  </div>
  <button class="btn_menu_toolbar btn_subscription #subscribe" data-blog-id="5646409" data-device="web_pc" data-tiara-action-name="구독 버튼_클릭" data-url="https://code-chy.tistory.com/183" type="button">
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
     <a href="/181">
      시그널, 쉘, 마운트, Sticky Bit
     </a>
     <span>
      (0)
     </span>
    </th>
    <td>
     2024.11.11
    </td>
   </tr>
  </table>
 </div>
 <!-- PostListinCategory - END -->
</div>
