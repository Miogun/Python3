import datetime

today = datetime.now()
year = today.strftime('%Y년')
print(f"오늘은 {today:%Y년 today:%M월, today:%d일}입니다.")
