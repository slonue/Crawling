import requests
from bs4 import BeautifulSoup

url = 'https://www.agoda.com/'

# 웹 페이지 가져오기
response = requests.get(url)

# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 호텔 이름 추출
hotel_names = soup.select('.hotel-name')  # 해당 클래스명은 아고다 페이지의 실제 HTML 구조에 맞게 수정해주세요
for hotel_name in hotel_names:
    print(hotel_name.text.strip())
