# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 09:44:47 2024

@author: kkadi
"""

import yfinance as yf
import datetime

# IRP_개인연금 정보
dic_pension_irp =  {
                        # 보유 수량 입력
                        'list_hold_num'     : [ 178,
                                               776,
                                               505,
                                               74,
                                               25 ],
                        # 추가 투자금
                        'money_add_won'     : 1085000,

                        # stock name 
                        'list_stock_name'   : [ "kodex_bank",
                                                "arirang_msci",
                                                "tiger_SnP_500",
                                                "kosef_nbond10y",
                                                "kodex_sbond"],
                        # standard stock number
                        'list_stock_number' : ['091170.KS',
                                               '195980.KS', 
                                               '360750.KS', 
                                               '148070.KS', 
                                               '153130.KS'],
                        # 목표 비율
                        'list_portion'      : [ 5.0,
                                               25.0,
                                               30.0,
                                               30.0,
                                               10.0]
                        
                   }

# 연금저축 정보
dic_pension =  {
                        # 보유 수량 입력
                        'list_hold_num'     : [ 318,
                                               1447,
                                               105,
                                               1727,
                                               365,
                                               146,
                                               75],
                        # 추가 투자금
                        'money_add_won'     : 1317208,

                        # stock name 
                        'list_stock_name'   : [ "gold",
                                                "kodex_usbond10y",
                                                "kodex_bank",
                                                "arirang_msci",
                                                "tiger_SnP500",
                                                "kosef_nbond10y",
                                                "kodex_sbond"
                                              ],
                        # standard stock number
                        'list_stock_number' : ['132030.KS',
                                               '308620.KS',
                                               '091170.KS',
                                               '195980.KS',
                                               '143850.KS',
                                               '148070.KS',
                                               '153130.KS'
                                               ],
                        # 목표 비율
                        'list_portion'      : [ 5.0,
                                               20.0,
                                                1.0,
                                               19.0,
                                               25.0,
                                               20.0,
                                               10.0
                                              ]
                   }

# 계산할 정보 선택
PENSION = 0     # 연금 ( 연금저축 )
PENSION_IRP = 1 # 연금IRP ( 개인연금 IRP )

#mode = PENSION
mode = PENSION_IRP

if mode == PENSION:
    list_stock_name = dic_pension_irp['list_stock_name']
    list_stock_number = dic_pension_irp['list_stock_number']
    list_hold_num = dic_pension_irp['list_hold_num']
    list_portion = dic_pension_irp['list_portion']
    money_add_won = dic_pension_irp['money_add_won']
elif mode == PENSION_IRP:
    list_stock_name = dic_pension['list_stock_name']
    list_stock_number = dic_pension['list_stock_number']
    list_hold_num = dic_pension['list_hold_num']
    list_portion = dic_pension['list_portion']
    money_add_won = dic_pension['money_add_won']
else:
    print('invalid mode = {}'.format(mode))
    list_stock_name = [];
    list_stock_number = [];
    list_hold_num = [];
    list_portion = [];
    money_add_won = [];

# 오늘로 부터 날짜 이동 ( 며칠전 부터 ? )
DAY_SHIFT = 5   

# 주가 추출할 날짜 수 ( 며칠동안 ? )
DAY_LENGTH = 3

# 시작 날짜
day_start = datetime.date.today() - datetime.timedelta(DAY_SHIFT)

# 마치는 날짜
day_end = day_start + datetime.timedelta(DAY_LENGTH)

# 날짜 사이 주가 추출
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
print()
print()
for stock_name, change_num in zip(list_stock_name, list_change_num):
    print(stock_name+"     : {:.1f} " .format(change_num))

