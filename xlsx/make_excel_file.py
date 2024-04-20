import numpy as np
import pandas as pd

X_NUM = 5           # touch sensor number on x-axis
Y_NUM = 5
BLOCK_REPEAT = 3    # repeat of x_num * y_num     

# 5x5 임의 숫자 데이터 블럭 생성
data_block = np.random.randint(1, 101, size=(Y_NUM*BLOCK_REPEAT, X_NUM))

# 데이터 블럭 배열을 DataFrame으로 변환
df = pd.DataFrame(data_block)

# 다섯 행마다 빈 행 추가
for i in range(0, len(df), Y_NUM):
    df.loc[i + Y_NUM] = pd.Series(np.nan, df.columns)

# 엑셀 파일 저장
df.to_excel('5x5_data_blocks_with_gaps.xlsx', index=False, header=False)
