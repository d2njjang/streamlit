============================================
1. c url 을 컨버팅한 코드 작성
============================================

import requests

cookies = {
    'NAC': 'fy5GCABTmweeE',
    'NNB': 'POQIQ3VVBGUGO',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '4100000000',
    '_fwb': '2822mnjwK7KrhQ4ppK031c.1740097918618',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '2822mnjwK7KrhQ4ppK031c.1740097918618',
    'NACT': '1',
    'SRT30': '1740276799',
    'SRT5': '1740276799',
    'REALESTATE': 'Sun%20Feb%2023%202025%2011%3A13%3A36%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'BUC': 'QuCnJVKpftzR-H_rr7vo3TIAIol2aZu562bx4tTBtZs=',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDAyNzY4MTYsImV4cCI6MTc0MDI4NzYxNn0.eIaOAg5jFR_cprKYpljfa3gLn_h5eOiZZEKXt2XA91w',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/109412?ms=37.243827,127.049093,17&a=APT:ABYG:JGC:PRE&e=RETAIL&ad=true',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    # 'cookie': 'NAC=fy5GCABTmweeE; NNB=POQIQ3VVBGUGO; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=4100000000; _fwb=2822mnjwK7KrhQ4ppK031c.1740097918618; landHomeFlashUseYn=Y; _fwb=2822mnjwK7KrhQ4ppK031c.1740097918618; NACT=1; SRT30=1740276799; SRT5=1740276799; REALESTATE=Sun%20Feb%2023%202025%2011%3A13%3A36%20GMT%2B0900%20(Korean%20Standard%20Time); BUC=QuCnJVKpftzR-H_rr7vo3TIAIol2aZu562bx4tTBtZs=',
}

response = requests.get(
    'https://new.land.naver.com/api/articles/complex/109412?realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=A1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=false&sameAddressGroup=true&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&page=5&complexNo=109412&buildingNos=&areaNos=&type=list&order=prc',
    cookies=cookies,
    headers=headers,
)

  "articleList": [
        {
            "articleNo": "2509434999",
            "articleName": "힐스테이트영통",
            "articleStatus": "R0",
            "realEstateTypeCode": "APT",
            "realEstateTypeName": "아파트",
            "articleRealEstateTypeCode": "A01",
            "articleRealEstateTypeName": "아파트",
            "tradeTypeCode": "A1",
            "tradeTypeName": "매매",
            "verificationTypeCode": "OWNER",
            "floorInfo": "고/27",
            "priceChangeState": "SAME",
            "isPriceModification": false,
            "dealOrWarrantPrc": "10억 7,000",
            "areaName": "111A",
            "area1": 111,
            "area2": 84,
            "direction": "남서향",
            "articleConfirmYmd": "20250221",
            "siteImageCount": 0,
            "articleFeatureDesc": "33A 방3 알파룸확장서재형,냉장고장,화이트필름 관리잘된집,트인뷰로채광굿",
            "tagList": [
                "10년이내",
                "대단지",
                "방세개",
                "화장실두개"
            ],
            "buildingName": "105동",
            "sameAddrCnt": 4,
            "sameAddrDirectCnt": 0,
            "sameAddrMaxPrc": "10억 7,000",
            "sameAddrMinPrc": "10억 7,000",
            "cpid": "bizmk",
            "cpName": "매경부동산",
            "cpPcArticleUrl": "http://land.mk.co.kr/rd/rd.php?UID=2509434999",
            "cpPcArticleBridgeUrl": "",
            "cpPcArticleLinkUseAtArticleTitleYn": false,
            "cpPcArticleLinkUseAtCpNameYn": true,
            "cpMobileArticleUrl": "",
            "cpMobileArticleLinkUseAtArticleTitleYn": false,
            "cpMobileArticleLinkUseAtCpNameYn": false,
            "latitude": "37.244124",
            "longitude": "127.047654",
            "isLocationShow": false,
            "realtorName": "힐스테이트영통공인중개사사무소",
            "realtorId": "lcewww",
            "tradeCheckedByOwner": false,
            "isDirectTrade": false,
            "isInterest": false,
            "isComplex": true,
            "detailAddress": "",
            "detailAddressYn": "N",
            "isVrExposed": false
        },

응답 코드를 참고해서 파이썬 코드를 완성해 주세요
이때 csv 형태로 부동산 호가 데이터를 저장하도록 해주세요
csv 파일에 한글이 깨지지 않도록 해주세요
url 값에 page 가 들어 있습니다. 1부터 10페이지까지 수집되도록 변경해 주세요
articleFeatureDesc 키가 특정 기사에 존재하지 않는 경우 기본값을 반환하도록 코드를 수정해줘
tradeTypeName 은 매매로만 표시해주고 23평~26평만 표시해줘, 4층 이상만 표시해줘
floorInfo가 숫자인 경우에만 변환하고, 그렇지 않은 경우에는 무시하도록 해줘   
층에 저라고 표시된 경우 1층으로 변환해줘

============================================
아래 코드는 정상 표시하는 코드임
============================================
import requests
import pandas as pd
from datetime import datetime
import json

def get_floor_number(floor_info):
    if not floor_info or '/' not in floor_info:
        return None
    
    floor, total = floor_info.split('/')
    if floor == '저':
        return 1
    try:
        return int(floor)
    except ValueError:
        return None

def convert_area_to_pyeong(area_m2):
    return area_m2 / 3.3058

def get_real_estate_data():
    cookies = {
        'NAC': 'fy5GCABTmweeE',
        'NNB': 'POQIQ3VVBGUGO',
        'nhn.realestate.article.rlet_type_cd': 'A01',
        'nhn.realestate.article.trade_type_cd': '""',
        'nhn.realestate.article.ipaddress_city': '4100000000',
        '_fwb': '2822mnjwK7KrhQ4ppK031c.1740097918618',
        'landHomeFlashUseYn': 'Y',
        'NACT': '1',
        'SRT30': '1740276799',
        'SRT5': '1740276799',
        'REALESTATE': 'Sun%20Feb%2023%202025%2011%3A13%3A36%20GMT%2B0900%20(Korean%20Standard%20Time)',
        'BUC': 'QuCnJVKpftzR-H_rr7vo3TIAIol2aZu562bx4tTBtZs=',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDAyNzY4MTYsImV4cCI6MTc0MDI4NzYxNn0.eIaOAg5jFR_cprKYpljfa3gLn_h5eOiZZEKXt2XA91w',
        'priority': 'u=1, i',
        'referer': 'https://new.land.naver.com/complexes/109412',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    }

    url = 'https://new.land.naver.com/api/articles/complex/109412?realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=A1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=false&sameAddressGroup=true&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&complexNo=109412&buildingNos=&areaNos=&type=list&order=prc'

    all_data = []

    try:
        response = requests.get(url, cookies=cookies, headers=headers)
        response.raise_for_status()
        
        print(f"Response Status: {response.status_code}")
        data = response.json()
        
        print(f"Response structure: {data.keys()}")
        
        if 'articleList' not in data:
            print("No articleList found in response")
            return all_data
            
        articles = data['articleList']
        print(f"Found {len(articles)} articles")

        for article in articles:
            floor = get_floor_number(article.get('floorInfo', ''))
            area_pyeong = convert_area_to_pyeong(article.get('area1', 0))
            
            print(f"Processing article: {article.get('articleNo', '')}")
            print(f"Area: {area_pyeong} pyeong, Floor: {floor}")
            
            # 26.317381571782928평은 약 26평이므로 포함시킵니다
            if 23 <= round(area_pyeong) <= 26 and (floor is not None and floor >= 4):
                print(f"Article {article.get('articleNo', '')} passed filters")
                all_data.append({
                    '매물번호': article.get('articleNo', ''),
                    '아파트명': article.get('articleName', ''),
                    '거래유형': '매매',
                    '가격': article.get('dealOrWarrantPrc', ''),
                    '면적(m²)': article.get('area1', ''),
                    '면적(평)': round(area_pyeong, 1),  # 소수점 첫째자리까지만 표시
                    '층수': floor,
                    '방향': article.get('direction', ''),
                    '특징': article.get('articleFeatureDesc', '정보 없음'),
                    '건물명': article.get('buildingName', ''),
                    '등록일': article.get('articleConfirmYmd', '')
                })
            else:
                print(f"Article {article.get('articleNo', '')} filtered out")
            
    except requests.exceptions.RequestException as e:
        print(f"데이터 수집 중 오류 발생: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON 파싱 오류: {e}")
        print(f"Response content: {response.text[:200]}")

    print(f"Total collected data: {len(all_data)} items")
    return all_data

def save_to_csv(data):
    if not data:
        print("저장할 데이터가 없습니다. 데이터 수집 과정을 확인해주세요.")
        return
    
    df = pd.DataFrame(data)
    filename = f'real_estate_data_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"데이터가 {filename}에 저장되었습니다.")
    print(f"저장된 데이터 개수: {len(df)}행")
    print("\n데이터 미리보기:")
    print(df.head())

if __name__ == "__main__":
    print("데이터 수집을 시작합니다...")
    data = get_real_estate_data()
    save_to_csv(data)
    ============================================
아파트 이름을 입력받아서 표시할수 있게 해줘
    ============================================
import requests
import pandas as pd
from datetime import datetime
import json

def get_floor_number(floor_info):
    if not floor_info or '/' not in floor_info:
        return None
    
    floor, total = floor_info.split('/')
    if floor == '저':
        return 1
    try:
        return int(floor)
    except ValueError:
        return None

def convert_area_to_pyeong(area_m2):
    return area_m2 / 3.3058

def get_real_estate_data(complex_id):
    cookies = {
        'NAC': 'fy5GCABTmweeE',
        'NNB': 'POQIQ3VVBGUGO',
        'nhn.realestate.article.rlet_type_cd': 'A01',
        'nhn.realestate.article.trade_type_cd': '""',
        'nhn.realestate.article.ipaddress_city': '4100000000',
        '_fwb': '2822mnjwK7KrhQ4ppK031c.1740097918618',
        'landHomeFlashUseYn': 'Y',
        'NACT': '1',
        'SRT30': '1740276799',
        'SRT5': '1740276799',
        'REALESTATE': 'Sun%20Feb%2023%202025%2011%3A13%3A36%20GMT%2B0900%20(Korean%20Standard%20Time)',
        'BUC': 'QuCnJVKpftzR-H_rr7vo3TIAIol2aZu562bx4tTBtZs=',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDAyNzY4MTYsImV4cCI6MTc0MDI4NzYxNn0.eIaOAg5jFR_cprKYpljfa3gLn_h5eOiZZEKXt2XA91w',
        'priority': 'u=1, i',
        'referer': f'https://new.land.naver.com/complexes/{complex_id}',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    }

    url = f'https://new.land.naver.com/api/articles/complex/{complex_id}?realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=A1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=false&sameAddressGroup=true&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&complexNo={complex_id}&buildingNos=&areaNos=&type=list&order=prc'

    all_data = []

    try:
        response = requests.get(url, cookies=cookies, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        
        if 'articleList' not in data:
            return all_data
            
        articles = data['articleList']

        for article in articles:
            floor = get_floor_number(article.get('floorInfo', ''))
            area_pyeong = convert_area_to_pyeong(article.get('area1', 0))
            
            if 23 <= round(area_pyeong) <= 26 and (floor is not None and floor >= 4):
                all_data.append({
                    '매물번호': f"=HYPERLINK('https://new.land.naver.com/articles/{article.get('articleNo', '')}', '{article.get('articleNo', '')}')",
                    '아파트명': article.get('articleName', ''),
                    '거래유형': '매매',
                    '가격': article.get('dealOrWarrantPrc', ''),
                    '면적(m²)': article.get('area1', ''),
                    '면적(평)': round(area_pyeong, 1),
                    '층수': floor,
                    '방향': article.get('direction', ''),
                    '특징': article.get('articleFeatureDesc', '정보 없음'),
                    '건물명': article.get('buildingName', ''),
                    '등록일': article.get('articleConfirmYmd', '')
                })
            
    except requests.exceptions.RequestException as e:
        print(f"데이터 수집 중 오류 발생: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON 파싱 오류: {e}")

    return all_data

def save_to_csv(data):
    if not data:
        print("저장할 데이터가 없습니다.")
        return
    
    df = pd.DataFrame(data)
    filename = f'real_estate_data_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"데이터가 {filename}에 저장되었습니다.")

if __name__ == "__main__":
    complex_id = input("아파트 단지 ID를 입력하세요: ")
    print("데이터 수집을 시작합니다...")
    data = get_real_estate_data(complex_id)
    save_to_csv(data)
