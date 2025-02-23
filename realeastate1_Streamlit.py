import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import json
import time

def get_floor_number(floor_info):
    if not floor_info or '/' not in floor_info:
        return None
    
    floor, total = floor_info.split('/')
    if floor == '저':
        return 1
    elif floor == '중':
        return 7  # 중층은 대체로 4-7층이므로 7층으로 간주
    elif floor == '고':
        return 12  # 고층은 대체로 12층 이상이므로 12층으로 간주
    try:
        return int(floor)
    except ValueError:
        return None

def convert_area_to_pyeong(area_m2):
    return area_m2 / 3.3058

def convert_price_to_number(price_str):
    if not price_str:
        return float('inf')
    
    parts = price_str.split()
    total = 0
    
    for part in parts:
        if '억' in part:
            total += int(part.replace('억', '')) * 10000
        else:
            total += int(part.replace(',', ''))
    
    return total

def get_real_estate_data(complex_id):
    cookies = {
        # your cookies
    }

    headers = {
        # your headers
    }

    small_data = []  # 23-27평
    large_data = []  # 32평 이상
    
    for page in range(1, 6):
        url = f'https://new.land.naver.com/api/articles/complex/{complex_id}?realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=A1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=true&sameAddressGroup=true&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&complexNo={complex_id}&buildingNos=&areaNos=&type=list&order=prc&page={page}'
        
        try:
            response = requests.get(url, cookies=cookies, headers=headers)
            response.raise_for_status()
            data = response.json()
            
            if 'articleList' not in data or not data['articleList']:
                break
            
            for article in data['articleList']:
                floor = get_floor_number(article.get('floorInfo', ''))
                area_pyeong = convert_area_to_pyeong(article.get('area1', 0))
                rounded_pyeong = round(area_pyeong)
                
                if floor is not None and (floor >= 4 or article.get('floorInfo', '').split('/')[0] in ['중', '고']):
                    article_data = {
                        '매물번호': f'=HYPERLINK("https://new.land.naver.com/articles/{article.get("articleNo", "")}", "{article.get("articleNo", "")}")',
                        '아파트명': article.get('articleName', ''),
                        '거래유형': '매매',
                        '가격': article.get('dealOrWarrantPrc', ''),
                        '가격_정렬용': convert_price_to_number(article.get('dealOrWarrantPrc', '')),
                        '면적(m²)': article.get('area1', ''),
                        '면적(평)': round(area_pyeong, 1),
                        '층수': article.get('floorInfo', '').split('/')[0],  # 원래 층수 표시 유지
                        '방향': article.get('direction', ''),
                        '특징': article.get('articleFeatureDesc', '정보 없음'),
                        '건물명': article.get('buildingName', ''),
                        '등록일': article.get('articleConfirmYmd', '')
                    }
                    
                    if 23 <= rounded_pyeong <= 27:
                        small_data.append(article_data)
                    elif rounded_pyeong >= 32:
                        large_data.append(article_data)
        
        except requests.exceptions.RequestException as e:
            print(f"데이터 수집 중 오류 발생: {e}")
            continue
        except json.JSONDecodeError as e:
            print(f"JSON 파싱 오류: {e}")
            continue
        
        time.sleep(1)  # API 요청 간 딜레이 추가

    result = []
    # 23-27평 최저가 1개
    if small_data:
        result.append(min(small_data, key=lambda x: x['가격_정렬용']))
    # 32평 이상 최저가 1개
    if large_data:
        result.append(min(large_data, key=lambda x: x['가격_정렬용']))

    # 정렬용 필드 제거
    for item in result:
        del item['가격_정렬용']
    
    return result

def process_all_apartments():
    try:
        # Excel 파일 읽기
        apt_df = pd.read_excel('aptlist.xlsx')
        all_results = []
        
        st.write("데이터 수집을 시작합니다...")
        total_apts = len(apt_df)
        
        for idx, row in apt_df.iterrows():
            complex_id = str(row['complex_id'])  # Excel 파일의 컬럼명에 따라 조정 필요
            st.write(f"\n처리 중: {idx + 1}/{total_apts} - 단지 ID: {complex_id}")
            
            data = get_real_estate_data(complex_id)
            if data:
                all_results.extend(data)
            
            time.sleep(2)  # API 요청 간 딜레이
        
        if all_results:
            df = pd.DataFrame(all_results)
            filename = f'real_estate_data_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'
            with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
                # 20평대 시트 작성
                small_df = df[(df['면적(평)'] >= 23) & (df['면적(평)'] <= 27)]
                small_df.to_excel(writer, sheet_name='20평대', index=False)

                # 30평대 시트 작성
                large_df = df[df['면적(평)'] >= 32]
                large_df.to_excel(writer, sheet_name='30평대', index=False)

            st.write(f"\n데이터가 {filename}에 저장되었습니다.")
            st.write("\n수집된 매물 정보:")
            st.dataframe(df[['아파트명', '가격', '면적(평)', '층수', '방향', '특징']])
        else:
            st.write("\n저장할 데이터가 없습니다.")
            
    except FileNotFoundError:
        st.write("aptlist.xlsx 파일을 찾을 수 없습니다.")
    except Exception as e:
        st.write(f"오류 발생: {e}")

def main():
    st.title("Real Estate Data Collector")
    st.write(f"실행 날짜: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    if st.button("데이터 수집 시작"):
        process_all_apartments()

if __name__ == "__main__":
    main()
