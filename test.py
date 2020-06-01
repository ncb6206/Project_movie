import requests
from bs4 import BeautifulSoup


def naver_movie():
    url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200524&tg=5"
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html.parser")
    tags = soup.find_all("div", {"class": "tit5"})

    for idx, tag in enumerate(tags):

        print(idx + 1, tag.text)

print("현재상영 영화 평점 순위")
naver_movie()
