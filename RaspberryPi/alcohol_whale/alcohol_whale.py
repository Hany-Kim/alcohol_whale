from PySide6.QtWidgets import *
from alcohol_whale_ui import Ui_Form

class MyApp(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        pass

    price_range_val = 0
    alcohol_range_val = 0
    # page 연결 함수
    cur_page_num = 0

    def nextPage(self):
        global cur_page_num
        #현재 페이지 index 출력
        cur_page_num = self.stackedWidget.currentIndex()
        print(cur_page_num)
        self.stackedWidget.setCurrentIndex(cur_page_num+1)

    def pastPage(self):
        global cur_page_num
        cur_page_num = self.stackedWidget.currentIndex()
        print(cur_page_num)
        self.stackedWidget.setCurrentIndex(cur_page_num - 1)

    def move_home(self):
        self.stackedWidget.setCurrentWidget(self.page_1)

    def takeApicture(self):
        pass

    def send_kakao(self):
        pass

    def move_survey(self):
        self.stackedWidget.setCurrentWidget(self.page_3)

    def move_sentiment(self):
        self.stackedWidget.setCurrentWidget(self.page_15)

    def send_price_range(self):
        global price_range_val
        price_range_val = self.p3_price_rangeSlider.value()
        print(price_range_val)

    def send_alcohol_range(self):
        global alcohol_range_val
        alcohol_range_val = self.p5_price_rangeSlider.value()
        print(alcohol_range_val)

app = QApplication()
win = MyApp()

win.show()
app.exec()