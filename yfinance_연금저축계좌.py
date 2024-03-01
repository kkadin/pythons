# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 10:28:47 2024

@author: kkadi
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import yfinance as yf
import datetime

# 추가 투자금
money_add_won = 1153803

# 보유 수량 입력
hold_of_gold = 293
hold_of_kodex_usbond10y = 1395
hold_of_kodex_bank = 120
hold_of_arirang_msci = 1708
hold_of_tiger_SnP500 = 392
hold_of_kosef_nbond10y = 138
hold_of_kodex_sbond = 69


# 목표 비율
portion_of_gold = 5.0
portion_of_kodex_usbond10y = 20.0
portion_of_kodex_bank = 1.0
portion_of_arirang_msci = 19.0
portion_of_tiger_SnP500 = 25.0
portion_of_kosef_nbond10y = 20.0
portion_of_kodex_sbond = 10.0

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
# kosef_nbond10y = yf.download('148070.KS', start = day_data_get, end = day_data_get+ datetime.timedelta(1))
gold = yf.download('132030.KS', start = day_start, end = day_end)
kodex_usbond10y = yf.download('308620.KS', start = day_start, end = day_end)
kodex_bank = yf.download('091170.KS', start = day_start, end = day_end)
arirang_msci = yf.download('195980.KS', start = day_start, end = day_end)
tiger_SnP500 = yf.download('143850.KS', start = day_start, end = day_end)
kosef_nbond10y = yf.download('148070.KS', start = day_start, end = day_end)
kodex_sbond = yf.download('153130.KS', start = day_start, end = day_end)

# print(kosef_nbond10y)
# print(kodex_sbond)

# 현재 주가 가져오기
# kosef_nbond10y = yf.download('148070.KS', start = day_now, end = day_now)
# print(kosef_nbond10y)

# print(tiger_SnP500)

# 평균값 구하기
# close_mean = tiger_SnP500["Close"].mean()
# print("\n")
# print("tiger_SnP500[\"Close\"]")
# print(tiger_SnP500["Close"])
# print("\n")
# print("close_mean")
# print(close_mean)

# 평균값 구하기
close_mean_gold = gold["Close"].mean()
close_mean_kodex_usbond10y = kodex_usbond10y["Close"].mean()
close_mean_kodex_bank = kodex_bank["Close"].mean()
close_mean_arirang_msci = arirang_msci["Close"].mean()
close_mean_tiger_SnP500 = tiger_SnP500["Close"].mean()
close_mean_kosef_nbond10y = kosef_nbond10y["Close"].mean()
close_mean_kodex_sbond = kodex_sbond["Close"].mean()

# print("")
# print("close_mean_kodex_bank")
# print(close_mean_kodex_bank)
# print("close_mean_arirang_msci")
# print(close_mean_arirang_msci)
# print("close_mean_tiger_SnP500")
# print(close_mean_tiger_SnP500)
# print("close_mean_kosef_nbond10y")
# print(close_mean_kosef_nbond10y)
# print("close_mean_kodex_sbond")
# print(close_mean_kodex_sbond)

# _kodex_bank
# _arirang_msci
# _tiger_SnP500
# _kosef_nbond10y
# _kodex_sbond

# 총액 : 현재 평균값 * 보유수량 
total_gold = close_mean_gold * hold_of_gold
total_kodex_usbond10y = close_mean_kodex_usbond10y * hold_of_kodex_usbond10y
total_kodex_bank = close_mean_kodex_bank * hold_of_kodex_bank
total_arirang_msci = close_mean_arirang_msci * hold_of_arirang_msci
total_tiger_SnP500 = close_mean_tiger_SnP500 * hold_of_tiger_SnP500
total_kosef_nbond10y = close_mean_kosef_nbond10y * hold_of_kosef_nbond10y
total_kodex_sbond = close_mean_kodex_sbond * hold_of_kodex_sbond

array_total = [
            total_gold,
            total_kodex_usbond10y,            
            total_kodex_bank,
            total_arirang_msci,
            total_tiger_SnP500,
            total_kosef_nbond10y,
            total_kodex_sbond            
        ]

# sum of total
sum_of_total = 0

num_of_stocks = 7

for i in range(num_of_stocks):
    sum_of_total += array_total[i]

# 목표 금액
target_gold           = (sum_of_total + money_add_won)*portion_of_gold/100
target_kodex_usbond10y= (sum_of_total + money_add_won)*portion_of_kodex_usbond10y/100
target_kodex_bank     = (sum_of_total + money_add_won)*portion_of_kodex_bank/100
target_arirang_msci   = (sum_of_total + money_add_won)*portion_of_arirang_msci/100
target_tiger_SnP500   = (sum_of_total + money_add_won)*portion_of_tiger_SnP500/100
target_kosef_nbond10y = (sum_of_total + money_add_won)*portion_of_kosef_nbond10y/100
target_kodex_sbond    = (sum_of_total + money_add_won)*portion_of_kodex_sbond/100

# 매매 수량
change_num_gold = (target_gold - total_gold) / close_mean_gold
change_num_kodex_usbond10y = (target_kodex_usbond10y - total_kodex_usbond10y) / close_mean_kodex_usbond10y
change_num_kodex_bank = (target_kodex_bank - total_kodex_bank) / close_mean_kodex_bank
change_num_arirang_msci = (target_arirang_msci - total_arirang_msci) / close_mean_arirang_msci
change_num_tiger_SnP500 = (target_tiger_SnP500 - total_tiger_SnP500) / close_mean_tiger_SnP500
change_num_kosef_nbond10y = (target_kosef_nbond10y - total_kosef_nbond10y) / close_mean_kosef_nbond10y
change_num_kodex_sbond = (target_kodex_sbond - total_kodex_sbond) / close_mean_kodex_sbond

# 매매 수량 프린트
print()
print()
print("trading stock numbers")
print("gold           : {:.1f} " .format(change_num_gold))
print("kodex_usbond10y: {:.1f} " .format(change_num_kodex_usbond10y))
print("kodex_bank     : {:.1f} " .format(change_num_kodex_bank))
print("arirang_msci   : {:.1f} " .format(change_num_arirang_msci))
print("tiger_SnP500   : {:.1f} " .format(change_num_tiger_SnP500))
print("kosef_nbond10y : {:.1f} " .format(change_num_kosef_nbond10y))
print("kodex_sbond    : {:.1f} " .format(change_num_kodex_sbond))


