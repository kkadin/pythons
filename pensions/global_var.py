#사용방법
# 1. hold num update
# 2. money_add_xx update
# 3. 계산할 mode 선택

# 연금저축 정보
list_pension =  [ 
                        {'hold_num':118,    'name':"kodex_bank",      'number':'091170.KS', 'portion':  1.0},
                        {'hold_num':150,    'name':"gold_h",          'number':'132030.KS', 'portion':  2.5},
                        {'hold_num':182,    'name':"tiger_SnP500_h",  'number':'143850.KS', 'portion': 12.0},
                        {'hold_num':152,    'name':"kosef_nbond10y",  'number':'148070.KS', 'portion': 20.0},
                        {'hold_num':77,     'name':"kodex_sbond",     'number':'153130.KS', 'portion': 10.0},
                        {'hold_num':1727,   'name':"arirang_msci_h",  'number':'195980.KS', 'portion': 19.0},
                        {'hold_num':1509,   'name':"kodex_usbond10y", 'number':'308620.KS', 'portion': 20.0},
                        {'hold_num':729,    'name':"tiger_SnP500",    'number':'360750.KS', 'portion': 13.0},
                ]

# IRP_개인연금 정보
list_pension_irp =  [ 
                        {'hold_num':185,    'name':"kodex_bank",      'number':'091170.KS', 'portion': 5.0},
                        {'hold_num':795,    'name':"arirang_msci",    'number':'195980.KS', 'portion':25.0},
                        {'hold_num':496,    'name':"tiger_SnP_500",   'number':'360750.KS', 'portion':30.0},
                        {'hold_num':77,     'name':"kosef_nbond10y",  'number':'148070.KS', 'portion':30.0},
                        {'hold_num':26,     'name':"kodex_sbond",     'number':'153130.KS', 'portion':10.0}
                    ]

# 추가 납입할 금액
money_add_pension = 1000000
money_add_pension_irp = 0

# 계산할 정보 선택
PENSION = 0     # 연금 ( 연금저축 )
PENSION_IRP = 1 # 연금IRP ( 개인연금 IRP )

# mode 선택 ( 둘중에 하나만 # 해제 )
# mode = PENSION_IRP
mode = PENSION

# 지난 주가 계산할 날짜 범위 선택
DAY_SHIFT = 5   # 오늘로 부터 날짜 이동 ( 며칠전 부터 ? )
DAY_LENGTH = 3  # 주가 추출할 날짜 수 ( 며칠동안 ? )

