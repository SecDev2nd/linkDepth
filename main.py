import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_links(url, depth):
    if depth == 0:
        return []
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser', from_encoding="utf-8")

        links = soup.find_all('a', href=True)
        
        valid_links = []
        for link in links:
            href = link['href']
            if not href.startswith('javascript:'): 
                full_url = urljoin(url, href)
                valid_links.append(full_url)
                valid_links.extend(get_links(full_url, depth - 1))
        
        # 중복 링크 제거
        valid_links = list(set(valid_links))
        
        return valid_links
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# 시작 URL과 원하는 깊이를 지정하세요.
start_url = "https://comic.naver.com/webtoon"
depth = 5

links = get_links(start_url, depth)
for link in links:
    print(link)
