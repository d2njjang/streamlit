import requests
import pandas as pd
from urllib.parse import quote
import streamlit as st

def main():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.diningcode.com',
        'Referer': 'https://www.diningcode.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Whale/4.30.291.11 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="132", "Whale";v="4", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    st.title('지역 기반 맛집 검색')

    region = st.text_input("검색할 지역명을 입력하세요:", "")

    if region:
        restaurant_list = []

        for page in range(1, 6):
            data = {
                'query': region,
                'addr': '',
                'keyword': '',
                'order': 'r_score',
                'distance': '',
                'rn_search_flag': 'on',
                'search_type': 'poi_search',
                'lat': '',
                'lng': '',
                'rect': '',
                's_type': '',
                'token': '',
                'mode': 'poi',
                'dc_flag': '1',
                'page': str(page),
                'size': '20',
            }

            response = requests.post('https://im.diningcode.com/API/isearch/', headers=headers, data=data)
            if response.status_code == 200:
                response_data = response.json()
                restaurants = response_data["result_data"]["poi_section"]["list"]
                restaurant_list.extend(restaurants)
            else:
                st.error(f"Error: {response.status_code} on page {page}")
                break

        if restaurant_list:
            df = pd.DataFrame(restaurant_list)

            # 중요한 컬럼 정의 - 이름(상호명), 전화번호, 카테고리, 평점, 리뷰 횟수
            important_columns = {
                'nm': '이름',
                'phone': '전화번호',
                'category': '카테고리',
                'score': '평점',
                'review_cnt': '리뷰 횟수'  # 리뷰 횟수 컬럼 추가
            }

            df = df[list(important_columns.keys())]
            df = df.rename(columns=important_columns)

            # 네이버 지도 링크를 상호명으로 추가
            df['네이버 지도 링크'] = df['이름'].apply(lambda x: f"https://map.naver.com/v5/search/{quote(x)}")

            # HTML 링크 형식으로 변경하여 이름 클릭 시 네이버 지도 링크로 연결되도록 설정
            df['이름'] = df.apply(lambda row: f'<a href="{row["네이버 지도 링크"]}" target="_blank">{row["이름"]}</a>', axis=1)
            df = df.drop(columns=['네이버 지도 링크'])  # 네이버 지도 링크 열 삭제

            # Ensure that the '평점' and '리뷰 횟수' columns are numeric for accurate sorting
            df['평점'] = pd.to_numeric(df['평점'], errors='coerce')
            df['리뷰 횟수'] = pd.to_numeric(df['리뷰 횟수'], errors='coerce')

            # Sort the DataFrame by the '평점' column in descending order
            df = df.sort_values(by='평점', ascending=False)

            # Add rank column
            df.insert(0, '순위', range(1, len(df) + 1))

            # Display the DataFrame in Streamlit with HTML rendering
            st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)

            # Save the sorted DataFrame to a CSV file for download
            output_file = f"restaurants_{region}.csv"
            df.to_csv(output_file, index=False, encoding='utf-8-sig')
            st.success(f"Data has been written to {output_file} successfully.")
            st.download_button(
                label="Download CSV",
                data=open(output_file, 'rb').read(),
                file_name=output_file,
                mime='text/csv'
            )
        else:
            st.warning("No data found for the specified region.")

if __name__ == "__main__":
    main()