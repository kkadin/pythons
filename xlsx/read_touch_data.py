# 라이브러리 import
import pandas as pd
import matplotlib.pyplot as plt
import os

print('current dir : {}'.format(os.getcwd()))
os.chdir('D:/software/python/test')

# 엑셀 파일 읽어오기
# xls = pd.ExcelFile('test.xlsx')

# Now you can list all sheets in the file
# xls.sheet_names

# df = pd.read_excel("test.xlsx")
df = pd.read_excel('test_2.xlsx',engine='openpyxl')
#df = pd.read_excel("test01.py")

df = df.set_axis(['1', '2', '3', '4', '5'], axis=1)

ROWS_OF_A_TOUCH_FRAME_IN_DF = 7     # data frame 에서 touch frame이 차이하는 행 갯수
START_ROW_OF_SENSOR = 3
COLUMN_OF_SENSOR = 4

# 30 행 마다 반복되는 셀 값 리스트에 저장
data = []
# for i in range(0, len(df), 7):
for row in range(START_ROW_OF_SENSOR, len(df), ROWS_OF_A_TOUCH_FRAME_IN_DF):
    data.append(df.iloc[row, COLUMN_OF_SENSOR])

# 그래프 그리기
plt.plot(data)
plt.xlabel('row number')
plt.ylabel('touch intensity')
plt.show()

a = 1
print(a)