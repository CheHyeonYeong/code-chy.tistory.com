import feedparser
import os

# RSS 피드 가져오기
rss_url = "https://code-chy.tistory.com/rss"
rss = feedparser.parse(rss_url)

# README.md 파일 읽기
readme_path = "README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

# RSS 데이터 활용하여 새로운 포스트 추가
post = ""
for feed in rss['entries']:
    date = f"{feed.published_parsed.tm_year}.{feed.published_parsed.tm_mon}.{feed.published_parsed.tm_mday}"
    check = f"{date} : {feed.title}"
    
    # 이미 추가된 포스트인지 확인
    if check not in content:
        post += f"[{date} : {feed.title}]({feed.link}) <br>\n"

# README.md 파일 갱신
if post:
    with open(readme_path, "a", encoding="utf-8") as f:
        f.write(post)

    # GitHub에 자동 푸시
    os.system("git add README.md")
    os.system('git commit -m "Update README.md with latest blog posts"')
    os.system("git push origin main")  # 브랜치 이름이 다르면 'main'을 변경해야 함
