import feedparser
import requests
from bs4 import BeautifulSoup
import os

# ✅ 저장할 폴더 생성
POSTS_DIR = "posts"
os.makedirs(POSTS_DIR, exist_ok=True)

# ✅ 기존 저장된 파일 목록 가져오기
def get_existing_posts():
    existing_posts = set()
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md"):
            existing_posts.add(filename)  # 기존 파일 이름 저장
    return existing_posts

# ✅ RSS에서 모든 블로그 글 가져오기
def get_all_posts():
    all_posts = []
    rss_url = "https://code-chy.tistory.com/rss"  # 🔹 Tistory 블로그 RSS 주소
    rss = feedparser.parse(rss_url)

    for entry in rss.entries:
        post_data = {
            "title": entry.title,
            "link": entry.link,
            "date": f"{entry.published_parsed.tm_year}-{entry.published_parsed.tm_mon:02d}-{entry.published_parsed.tm_mday:02d}",
            "content": get_post_content(entry.link)  # ✅ 블로그 본문 가져오기
        }
        all_posts.append(post_data)

    return all_posts

# ✅ 개별 블로그 글의 본문 가져오기
def get_post_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # 🔹 본문 내용을 가져올 수 있는 div 선택
        content_div = soup.select_one("div.area_view#article-view")  # Tistory 본문 영역

        if not content_div:
            return "❌ 본문을 가져올 수 없습니다."

        # 🔹 HTML 태그 포함하여 본문 가져오기
        return str(content_div)

    except Exception as e:
        return f"오류 발생: {e}"

# ✅ 블로그 글을 개별 `.md` 파일로 저장 (새로운 글만 추가)
def save_posts_as_md(posts):
    existing_files = get_existing_posts()  # 기존 파일 목록 가져오기
    new_files_added = False  # 새로운 글 추가 여부 확인

    for post in posts:
        safe_title = post['title'].replace(" ", "_").replace("/", "_")  # 🔹 파일명 문제 방지
        filename = f"{post['date']}-{safe_title}.md"
        filepath = os.path.join(POSTS_DIR, filename)  # 🔹 안전한 파일 경로

        if filename in existing_files:
            print(f"🚫 이미 저장됨: {filename}, 건너뜀!")
            continue  # 이미 저장된 글이면 건너뜀

        md_content = f"# {post['title']}\n\n"
        md_content += f"📅 {post['date']}\n\n"
        md_content += f"[원문 링크]({post['link']})\n\n"
        md_content += "---\n\n"
        md_content += post['content']  # 🔹 HTML 포함된 본문 추가

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md_content)

        print(f"✅ 새 글 저장됨: {filename}")
        new_files_added = True  # 새로운 파일이 추가됨

    return new_files_added  # 새로운 파일 추가 여부 반환

# ✅ GitHub에 자동 푸시 (새로운 파일이 있을 때만)
def git_push():
    os.system("git add posts/")
    commit_message = "Auto-update: New blog posts added"
    os.system(f'git commit -m "{commit_message}" || echo "No new changes to commit"')
    os.system("git push origin main")

# ✅ 실행 (최종 동작)
if __name__ == "__main__":
    all_blog_posts = get_all_posts()  # 블로그 글 가져오기
    new_files_added = save_posts_as_md(all_blog_posts)  # 새로운 글 저장

    if new_files_added:  # 새로운 글이 추가된 경우에만 Git 커밋 & 푸시
        git_push()
    else:
        print("✅ 새로운 글이 없습니다. Git 커밋 생략!")
