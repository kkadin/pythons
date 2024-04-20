# 라이브러리 import
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

print('current dir : {}'.format(os.getcwd()))
#os.chdir('D:/software/python/test')
os.chdir('D:/software/python/pythons/xlsx')

df = pd.read_excel('5x5_data_blocks_with_gaps.xlsx', header = None) # do not use first row of the excel file
#df = pd.read_excel('test_2.xlsx')

ROWS_OF_A_TOUCH_FRAME_IN_DF = 6     # data frame 에서 touch frame이 차이하는 행 갯수
START_ROW_OF_SENSOR = 2
COLUMN_OF_SENSOR = 2

# sensor 값 가져오기
data = []
for row in range(START_ROW_OF_SENSOR, len(df), ROWS_OF_A_TOUCH_FRAME_IN_DF):
    data.append(df.iloc[row, COLUMN_OF_SENSOR])

# 정보 계산
max = np.max(data)
mean = np.mean(data)
noise = np.std(data)
snr = 20 * np.log10(mean/noise)

# 그래프 그리기
plt.plot(data)
y_max = mean * 2
plt.ylim(0, y_max)

# Write text on the plot
plt.text(len(data)/2, int(max), 'mean = {:.2f}, noise = {:.2f}, snr = {:.2f} '.format(mean, noise, snr), fontsize=12, color='red')

plt.xlabel('row number')
plt.ylabel('touch intensity')
plt.show()

# list_pos1 = data[2:5]
# y_max = max(list_pos1) * 2
# plt.ylim(0, y_max)
# plt.plot(list_pos1)
# plt.xlabel('row number')
# plt.ylabel('touch intensity')
# plt.show()
