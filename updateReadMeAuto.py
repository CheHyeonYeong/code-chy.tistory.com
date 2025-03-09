import feedparser
import requests
from bs4 import BeautifulSoup
import os

# ✅ 저장할 폴더 생성
POSTS_DIR = "posts"
os.makedirs(POSTS_DIR, exist_ok=True)

# ✅ RSS에서 모든 블로그 글 가져오기
def get_all_posts():
    rss_url = "https://code-chy.tistory.com/rss"
    rss = feedparser.parse(rss_url)

    all_posts = []
    for entry in rss.entries:
        post_data = {
            "title": entry.title,
            "link": entry.link,
            "date": f"{entry.published_parsed.tm_year}-{entry.published_parsed.tm_mon:02d}-{entry.published_parsed.tm_mday:02d}",
            "content": get_post_content(entry.link)  # ✅ 블로그 본문 가져오기
        }
        all_posts.append(post_data)

    return all_posts


# ✅ 개별 블로그 글의 본문 가져오기 (HTML 포함)
def get_post_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # 🔹 본문 내용을 가져올 수 있는 div 선택
        content_div = soup.select_one("div.area_view#article-view")

        if not content_div:
            return "❌ 본문을 가져올 수 없습니다."

        # 🔹 HTML 태그까지 유지한 상태로 저장
        return content_div.prettify()

    except Exception as e:
        return f"오류 발생: {e}"


# ✅ 블로그 글을 개별 `.md` 파일로 저장
def save_posts_as_md(posts):
    for post in posts:
        filename = f"{POSTS_DIR}/{post['date']}-{post['title'].replace(' ', '_')}.md"
        filename = filename.replace("/", "_")  # 파일명에 `/` 있으면 오류 나니까 변경

        md_content = f"# {post['title']}\n\n"
        md_content += f"📅 {post['date']}\n\n"
        md_content += f"[원문 링크]({post['link']})\n\n"
        md_content += "---\n\n"
        md_content += post['content']  # 🔹 HTML 포함된 본문 추가

        with open(filename, "w", encoding="utf-8") as f:
            f.write(md_content)

        print(f"✅ 저장됨: {filename}")


# ✅ 테스트용 실행
if __name__ == "__main__":
    all_blog_posts = get_all_posts()
    save_posts_as_md(all_blog_posts)
    print("✅ 테스트 완료")

# ✅ GitHub에 자동 푸시
def git_push():
    os.system("git add posts/")
    os.system('git commit -m "Auto-update blog posts as markdown" || echo "No changes to commit"')
    os.system("git push origin main")


# ✅ 실행
all_blog_posts = get_all_posts()
save_posts_as_md(all_blog_posts)
git_push()
