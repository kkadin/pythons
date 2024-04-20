# 라이브러리 import
import pandas as pd
import matplotlib.pyplot as plt
import os

print('current dir : {}'.format(os.getcwd()))
#os.chdir('D:/software/python/test')
os.chdir('D:/software/python/pythons/xlsx')

# df = pd.read_excel('5x5_data_blocks_with_gaps.xlsx',engine='openpyxl')
df = pd.read_excel('5x5_data_blocks_with_gaps.xlsx', header = None) # do not use first row of the excel file
#df = pd.read_excel('test_2.xlsx')

# df = df.set_axis(['1', '2', '3', '4', '5'], axis=1)

ROWS_OF_A_TOUCH_FRAME_IN_DF = 6     # data frame 에서 touch frame이 차이하는 행 갯수
START_ROW_OF_SENSOR = 2
COLUMN_OF_SENSOR = 2

# sensor 값 가져오기
data = []
for row in range(START_ROW_OF_SENSOR, len(df), ROWS_OF_A_TOUCH_FRAME_IN_DF):
    data.append(df.iloc[row, COLUMN_OF_SENSOR])

# 그래프 그리기
plt.plot(data)
plt.xlabel('row number')
plt.ylabel('touch intensity')
plt.show()

