import feedparser

def get_all_posts():
    all_posts = []
    page = 1

    while True:
        # Tistory의 RSS는 기본적으로 30개까지만 가져올 수 있으므로, page를 추가해서 요청
        rss_url = f"https://code-chy.tistory.com/rss?page={30}"
        rss = feedparser.parse(rss_url)

        if not rss.entries:  # 더 이상 가져올 데이터가 없으면 종료
            break

        for entry in rss.entries:
            post_data = {
                "title": entry.title,
                "link": entry.link,
                "date": f"{entry.published_parsed.tm_year}.{entry.published_parsed.tm_mon}.{entry.published_parsed.tm_mday}"
            }
            all_posts.append(post_data)

        page += 1  # 다음 페이지로 이동

    return all_posts

# 모든 포스트 출력
all_blog_posts = get_all_posts()
for post in all_blog_posts:
    print(f"{post['date']} - {post['title']} ({post['link']})")
