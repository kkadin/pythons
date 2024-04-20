import numpy as np
import pandas as pd

X_NUM = 5           # touch sensor number on x-axis
Y_NUM = 5           # touch sensor number on y-axis
Y_NUM_SPACE = 1     # row to be deleted
SENSOR_DATA = [0,1,3,2,3,1,0]
BLOCK_REPEAT = len(SENSOR_DATA)    # repeat of x_num * y_num     
X_SENSOR = 2        # target touch sensor x position
Y_SENSOR = 2        # target touch sensor y position

# 숫자 데이터 블럭 생성
data_block = np.random.randint(1, 101, size=((Y_NUM+Y_NUM_SPACE)*BLOCK_REPEAT, X_NUM))

# SENSOR_DATA를 매 block 마다 삽입
for block_idx in range(BLOCK_REPEAT):
    row_in_data_block = block_idx * (Y_NUM+Y_NUM_SPACE) + Y_SENSOR
    col_in_data_block = X_SENSOR
    row_in_sensor_data = block_idx
    data_block[row_in_data_block][col_in_data_block] = SENSOR_DATA[row_in_sensor_data]

# 데이터 블럭 배열을 DataFrame으로 변환
df = pd.DataFrame(data_block)

# 빈 행 생성
# for i in range(0, len(df), Y_NUM):
#     #df.loc[i + Y_NUM] = pd.Series(np.nan, df.columns)
#     df.loc[(i+1)*(Y_NUM+Y_NUM_SPACE)] = pd.Series(np.nan, df.columns)
for i in range(0, len(df), Y_NUM+Y_NUM_SPACE):
    #df.loc[i + Y_NUM] = pd.Series(np.nan, df.columns)
    row = i+(Y_NUM+Y_NUM_SPACE)-1
    df.loc[row] = pd.Series(np.nan, df.columns)

# 엑셀 파일 저장
df.to_excel('5x5_data_blocks_with_gaps.xlsx', index=False, header=False)
