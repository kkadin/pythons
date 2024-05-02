import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import os
from global_vars_for_qt import *

# sys.path.insert(0, 'D:/software/python/pythons/pensions')
# import global_var
# from global_var import *
# from my_file import my_variable

# import os
# dir_path = os.path.abspath('D:/software/python/pythons/pensions')
# sys.path.insert(0, dir_path)
# from global_var import *

print('current dir : {}'.format(os.getcwd()))
os.chdir('D:/software/python/pythons/qt_ui')

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
# form_class = uic.loadUiType("UI파일이름.ui")[0]
form_class = uic.loadUiType("test.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
# class WindowClass(QDialog, form_class) :
    def load_stock_hold_num(self):
        list_stock_info = list_pension

        list_stock_name = []
        list_stock_number = []
        list_hold_num = []
        list_portion = []
        for item in list_stock_info:
            list_stock_name.append(item['name']) 
            list_stock_number.append(item['number']) 
            list_hold_num.append(item['hold_num']) 
            list_portion.append(item['portion']) 
        
        self.lineEdit.setText(str(list_hold_num[0]))    
        # self.lineEdit.setText('init text')    


    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        # self.textbox.textChanged.connect(self.on_text_changed)
        # self.lineEdit.lineChanged.connect(self.on_line_changed)

        self.pushButton_Run.clicked.connect(self.button_event)
        self.load_stock_hold_num()

    # def on_line_changed(self, line):
    #     print(f"Line changed: {line}")

    def button_event(self):
        text = self.lineEdit.text() # line_edit text 값 가져오기
        self.label_test.setText(text) # label에 text 설정하기



if __name__ == "__main__":
    # import sys
    import os #<---change-1
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1" #<---change-2
    app = QApplication(sys.argv)
    MainWindow = WindowClass()
    MainWindow.show()
    sys.exit(app.exec_())

# if __name__ == "__main__" :
#     #QApplication : 프로그램을 실행시켜주는 클래스
#     app = QApplication(sys.argv) 

#     #WindowClass의 인스턴스 생성
#     myWindow = WindowClass() 

#     #프로그램 화면을 보여주는 코드
#     myWindow.show()

#     #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
#     app.exec_()


