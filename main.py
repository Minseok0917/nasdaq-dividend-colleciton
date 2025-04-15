from lib import create_folder_if_not_exists, file_exists, save_json_to_file, generate_dates_in_month, fetch_dividends_calendar


YEAR=2025
MONTH=4
DIVIDENDS_FOLDER = './dividends_calendar'
CURRENT_DIVIDENDS_FOLDER = f'{DIVIDENDS_FOLDER}/{YEAR}_{MONTH}'

create_folder_if_not_exists(CURRENT_DIVIDENDS_FOLDER)
for date in  generate_dates_in_month(year=YEAR, month=MONTH):
    if file_exists(date): continue

    response_json = fetch_dividends_calendar(date)
    save_json_to_file(response_json,f'{CURRENT_DIVIDENDS_FOLDER}/{date}.json')
    





