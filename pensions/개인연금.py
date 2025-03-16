# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 09:44:47 2024

@author: kkadi
"""
from global_var import *
import yfinance as yf
import datetime

list_hold_num = []              # 보유수량
list_stock_name = []
list_stock_number = []          # 주식 인식번호
list_portion = []

if mode == PENSION:
    list_stock_info = list_pension
    money_add_won = money_add_pension
elif mode == PENSION_IRP:
    list_stock_info = list_pension_irp
    money_add_won = money_add_pension_irp
else:
    print('invalid mode = {}'.format(mode))

for item in list_stock_info:
    list_hold_num.append(item['hold_num'])
    list_stock_number.append(item['number'])
    list_stock_name.append(item['name'])
    list_portion.append(item['portion'])

# 시작 날짜
day_start = datetime.date.today() - datetime.timedelta(DAY_SHIFT)

# 마치는 날짜
day_end = day_start + datetime.timedelta(DAY_LENGTH)

# 날짜 사이 주가 추출
# list_of_df_stock_data = []
list_close_mean = []
for item in list_stock_number:
    stock_data = yf.download(item, start = day_start, end = day_end)
    # stock_data = yf.download(item, start="2025-01-01", end="2025-01-10")
    # stock_data = yf.download("AAPL", start="2025-01-01", end="2025-01-10")
    # list_of_df_stock_data.append(stock_data)
    mean = stock_data["Close"].mean().iloc[0]
    list_close_mean.append(mean)

# 평균값 구하기
# list_close_mean = []
# for item in list_of_df_stock_data:
#     mean = item["Close"].mean()
#     list_close_mean.append(mean)

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
    # print("target:{} = (sum_of_total:{} + money_add_won:{}) * portion:{} / 100".format(target, sum_of_total, money_add_won, portion))
    list_target.append(target)

# 매매 수량
list_change_num = []
for target, total, close_mean in zip ( list_target, list_total, list_close_mean):
    change_num = (target - total)/close_mean
    list_change_num.append(change_num)

# 매매 수량 프린트
print()
print()
for stock_name, change_num in zip(list_stock_name, list_change_num):
    # rounded_num = int(round(change_num.iloc[0], 0))
    rounded_num = int(round(change_num, 0))
    print('{:>15}:{:>5}'.format(stock_name, rounded_num))

