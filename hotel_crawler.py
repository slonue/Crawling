import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = 'https://hotels.naver.com/'

# 웹 페이지 가져오기
response = requests.get(url)

# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 호텔 리스트 추출
hotel_list = soup.select('.Popular_hotel_list__vIw4R .item')

# 호텔 정보 추출 및 저장할 리스트 초기화
hotels_info = []

# 각 호텔의 정보 추출
for hotel in hotel_list:
    hotel_name = hotel.select_one('.Popular_hotelName__O95RW').text.strip()
    hotel_score = hotel.select_one('.Popular_score__khyaG').text.strip()
    hotel_price = hotel.select_one('.Popular_amount__YEn39').text.strip()
    hotel_grade = hotel.select_one('.Popular_star__X113Q').text.strip()
    
    # 호텔 정보를 딕셔너리로 저장
    hotel_info = {
        'Name': hotel_name,
        'Score': hotel_score,
        'Price': hotel_price,
        'Grade': hotel_grade
    }
    
    # 호텔 정보를 리스트에 추가
    hotels_info.append(hotel_info)

# 엑셀 파일 생성
wb = Workbook()
ws = wb.active

# 헤더 추가
ws.append(['Name', 'Score', 'Price', 'Grade'])

# 호텔 정보를 엑셀에 추가
for hotel in hotels_info:
    ws.append([hotel['Name'], hotel['Score'], hotel['Price'], hotel['Grade']])

# 엑셀 파일 저장
wb.save("hotel_info.xlsx")
