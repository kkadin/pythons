# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 09:44:47 2024

@author: kkadi
"""

import yfinance as yf
import datetime

# 추가 투자금
money_add_won = 729778

# 보유 수량 입력
list_hold_num = [ 199, 747, 525, 69, 23 ]


# 목표 비율
list_portion = [ 5.0, 25.0, 30.0, 30.0, 10.0]

# 오늘로 부터 날짜 이동 ( 며칠전 부터 ? )
DAY_SHIFT = 5   

# 주가 추출할 날짜 수 ( 며칠동안 ? )
DAY_LENGTH = 1

# 시작 날짜
day_start = datetime.date.today() - datetime.timedelta(DAY_SHIFT)

# 마치는 날짜
day_end = day_start + datetime.timedelta(DAY_LENGTH)

# 오늘 날짜
# day_now = datetime.date.today()
# day_end = day_now

# 5일전 날짜
# day_start = day_end - datetime.timedelta(5);
# day_data_get = day_now - datetime.timedelta(2)

# 날짜 사이 주가 추출
list_stock_number = ['091170.KS','195980.KS', '360750.KS', '148070.KS', '153130.KS']
list_stock_data = []
for item in list_stock_number:
    stock_data = yf.download(item, start = day_start, end = day_end)  
    list_stock_data.append(stock_data)

# 평균값 구하기
list_close_mean = []
for item in list_stock_data:
    mean = item["Close"].mean()
    list_close_mean.append(mean)

# 총액 : 현재 평균값 * 보유수량 
list_total = []
for close_mean, hold_num in zip(list_close_mean, list_hold_num):
    total = close_mean * hold_num
    list_total.append(total)

sum_of_total = sum(list_total)


# 목표 금액
list_target = []
for portion in list_portion:
    target = (sum_of_total + money_add_won) * portion/100
    list_target.append(target)


# 매매 수량
list_change_num = []
for target, total, close_mean in zip ( list_target, list_total, list_close_mean):
    change_num = (target - total)/close_mean
    list_change_num.append(change_num)

# 매매 수량 프린트
list_stock_name =   [
                        "kodex_bank",
                        "arirang_msci",
                        "tiger_SnP_500",
                        "kosef_nbond10y",
                        "kodex_sbond"
                    ]

print()
print()
for stock_name, change_num in zip(list_stock_name, list_change_num):
    print(stock_name+"     : {:.1f} " .format(change_num))

