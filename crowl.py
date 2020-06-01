import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import ssl
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["제목", "장르","정보"])


ssl._create_default_https_context = ssl._create_unverified_context

raw = requests.get("https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%97%AD%EB%8C%80+%EC%98%81%ED%99%94+%EC%88%9C%EC%9C%84",
                   headers={"User-Agent": "Mozilla/5.0"})

html = BeautifulSoup(raw.text, 'html.parser')
movies = html.select("dl.lst_dsc")
n=0
for m in movies:
    title = m.select_one("dt.tit a")
    url = title.attrs["href"]
    genre = m.select_one("dl.info_txt1 a")
    url = title.attrs["href"]

    print("=" * 50)
    print("영화 제목 : ", title.text.strip())
    print("영화 장르 : ", genre.text)
    print("정보 : https://movie.naver.com" + url)
    sheet.append([title.text.strip(), genre.text, "https://movie.naver.com"+url])
    wb.save("naver_moive_info.xlsx")

    each_raw = requests.get("https://movie.naver.com" + url,
                            headers={"User-Agent": "Mozilla/5.0"})

    each_html = BeautifulSoup(each_raw.text, 'html.parser')
    #genre = each_html.select_one("dl.list_main dd:nth-of-type(1)")

    # poster 선택자 : div.mv_info_area div.poster img
    poster = each_html.select_one("div.mv_info_area div.poster img")
    poster_src = poster.attrs["src"]

    urlretrieve(poster_src, "static/" + str(n) + ".png")
    n=n+1



    # title[:2]는 제목의 앞글자 두글자만 따겠다는 것인데, 특수문자가 제목에 들어있는 경우에는 파일 이름에 에러가 나기 때문이다.
    # 또 위에서 title변수가 아니라 출력문에 .text를 붙였기에 여기서도 .text를 붙여준다.