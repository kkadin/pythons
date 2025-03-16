# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 09:44:47 2024

@author: kkadi
"""
from global_var import *
import yfinance as yf
import datetime
import numpy as np
import pandas as pd
from tkinter import Tk, Text, END

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

# 주식 종목 가격 정보 정리 : 가능한 날짜의 종가를 averaging함.
# ! 현재 가격은 못가져 오나?
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

# # # report 작성
df_report = pd.DataFrame(list_stock_info)
# df_report['현재가격'] = pd.Series(list_close_mean)
df_report['current price'] = pd.Series(list_close_mean)


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

# df_report['총가격'] = pd.Series(list_total)
df_report['total value'] = pd.Series(list_total)


# 목표 금액
list_target = []
for portion in list_portion:
    target = (sum_of_total + money_add_won) * portion/100
    # print("target:{} = (sum_of_total:{} + money_add_won:{}) * portion:{} / 100".format(target, sum_of_total, money_add_won, portion))
    list_target.append(target)

df_report['target total'] = pd.Series(list_target)

# 매매 수량
list_change_num = []
for target, total, close_mean in zip ( list_target, list_total, list_close_mean):
    change_num = (target - total)/close_mean
    list_change_num.append(change_num)

df_report['trading'] = pd.Series(list_change_num)

df_report['hold_num_after_trading'] = pd.Series(np.array(list_hold_num) + np.array(list_change_num))
# df_report['total_after_trading'] = df_report['hold_num_after_trading'] * np.array(list_close_mean)
df_report['total_after_trading'] = df_report['hold_num_after_trading'].astype(int) * df_report['current price'].astype(int)

# Add a row with sums
df_report.loc[len(df_report)] = df_report.select_dtypes(include=[np.number]).sum()
df_report.loc[len(df_report)-1, 'hold_num'] = 0     # Override 'number'
df_report.loc[len(df_report)-1, 'name'] = ''        # Override 'name'
df_report.loc[len(df_report)-1, 'number'] = ''     # Override 'number'
df_report.loc[len(df_report)-1, 'current price'] = 0
df_report.loc[len(df_report)-1, 'trading'] = 0
df_report.loc[len(df_report)-1, 'hold_num_after_trading'] = 0


# np_arr_change_num = np.array(list_change_num)
# print(np_arr_change_num)
# print(np_arr_change_num.mean())

# 매매 수량 프린트
# print()
# print()
# for stock_name, change_num in zip(list_stock_name, list_change_num):
#     # rounded_num = int(round(change_num.iloc[0], 0))
#     rounded_num = int(round(change_num, 0))
#     print('{:>15}:{:>5}'.format(stock_name, rounded_num))

# Set float display format to show no decimal places
pd.options.display.float_format = '{:.0f}'.format
pd.set_option('display.max_rows', None)      # Show all rows
pd.set_option('display.max_columns', None)   # Show all columns
print(df_report.iloc[:,0:5])
print("added fund : {}".format(money_add_won))
print(df_report.iloc[:,5:10])

# Create a simple Tkinter window
# root = Tk()
# root.title("DataFrame Viewer")
# text = Text(root)
# text.insert(END, df_report.to_string())
# text.pack()
# root.mainloop()  # Keeps the window open until you close it