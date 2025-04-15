import os
import json
import requests
from datetime import datetime, timedelta


def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"📁 폴더 생성됨: {folder_path}")

def save_json_to_file(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def file_exists(file_path):
    return os.path.isfile(file_path)

def generate_dates_in_month(year: int, month: int):
    start_date = datetime(year, month, 1)
    
    # 다음 달 1일 만들고 하루 빼서 말일 계산
    if month == 12:
        next_month = datetime(year + 1, 1, 1)
    else:
        next_month = datetime(year, month + 1, 1)

    end_date = next_month - timedelta(days=1)

    # 날짜 리스트 만들기
    date_list = []
    current_date = start_date
    while current_date <= end_date:
        date_list.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)

    return date_list




def fetch_dividends_calendar(date):
    response = requests.get(f'https://api.nasdaq.com/api/calendar/dividends?date={date}', headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept': 'application/json',
    })
    return response.json()