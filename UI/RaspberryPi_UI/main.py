from PySide6.QtWidgets import *
#ui import
from mainUI import Ui_MainWindow

#사용자의 대답 저장
#2차원 배열 선언
YourAnswer = [[0 for column in range(10)]for row in range(10)]

#버튼 8개
btns = ["BTN1", "BTN2", "BTN3", "BTN4", "BTN5", "BTN6", "BTN7", "BTN8"]

#고정질문과 대답
questions = [
    " 원하는 가격대를 고르세요",
    " 좋아하는 맛과 향을 골라주세요",
    " 이대로면 취해버릴지 몰라~!!",
    " 다양한 종류가 있답니다",
    " 어떤 방법으로 마시는걸 좋아하시나요?",
]
#키값과 고른 대답을 함께 저장할 예정
answers = [
    ["~50,000", "50,000 ~ 100,000", "100,000~"],
    ["달달함", "고소함", "허브", "과일", "스모키", "초콜릿", "바닐라", "향신료"],
    ["~30%", "~50%", "상관없음"],
    ["위스키", "브랜디", "럼", "리큐르", "보드카"],
    ["칵테일,하이볼", "상관없음"]
]
keywords=["price","taste","alcohol", "gengre", "howto"]

#나중에는 DB에서 받아와야하는것들
#질문이 다르기때문에 키값을 함께 받아오는것이 편할듯->가능?
addedQ={
    "1": "오늘 피곤하신가요?",
    "2": "오늘 누구와 함께 술을 드실 예정인가요?",
    "3": "좋아하는 메뉴가 있는 식당에서 당신은 새로운 메뉴만 먹기 vs 색다른 메뉴 먹기 ?",
    "4": "가성비?",
    "5": "여행을 가신다면 어느 대륙으로 가고 싶으신가요?"
}
#키값과 대답을 함께 저장
choices={
    "1": ["네", "아니오"],
    "2": ["혼자", "친구", "연인", "가족", "선물"],
    "3": ["먹던거만", "새로운거"],
    "4": ["좋아", "가격?상관없지"],
    "5": ["유럽", "아시아", "아메리카대륙", "오세아니아"]
}


i = 0

#기본워딩
class My_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()
        self.showQs()
        self.hideAll()
        self.showQs()

    #질문 문항 보여주는 함수
    def main(self):
        global i, YourAnswer
        self.Questions.setText(questions[i])
        #첫번째에 문제코드
        YourAnswer[i][0] = i

    #버튼 초기화
    def hideAll(self):
        self.BTN1.hide()
        self.BTN2.hide()
        self.BTN3.hide()
        self.BTN4.hide()
        self.BTN5.hide()
        self.BTN6.hide()
        self.BTN7.hide()
        self.BTN8.hide()

    #답안 보여주는 함수
    def showQs(self):
        global i, answers
        n = len(answers[i])
        #확인용
        print("질문 : "+str(i)+", 답변:"+str(n))
        #갯수마다 위치고르기
        if n == 2:
            self.BTN3.setText(answers[i][0])
            self.BTN7.setText(answers[i][1])
            self.BTN3.show()
            self.BTN7.show()
        if n == 3:
            self.BTN1.setText(answers[i][0])
            self.BTN3.setText(answers[i][1])
            self.BTN5.setText(answers[i][2])
            self.BTN1.show()
            self.BTN3.show()
            self.BTN5.show()
        if n == 4:
            self.BTN1.setText(answers[i][0])
            self.BTN2.setText(answers[i][1])
            self.BTN5.setText(answers[i][2])
            self.BTN6.setText(answers[i][3])
            self.BTN1.show()
            self.BTN3.show()
            self.BTN5.show()
            self.BTN6.show()
        if n == 5:
            self.BTN1.setText(answers[i][0])
            self.BTN2.setText(answers[i][1])
            self.BTN3.setText(answers[i][2])
            self.BTN4.setText(answers[i][3])
            self.BTN5.setText(answers[i][4])
            self.BTN1.show()
            self.BTN2.show()
            self.BTN3.show()
            self.BTN4.show()
            self.BTN5.show()
        if n == 6:
            self.BTN1.setText(answers[i][0])
            self.BTN2.setText(answers[i][1])
            self.BTN3.setText(answers[i][2])
            self.BTN4.setText(answers[i][3])
            self.BTN5.setText(answers[i][4])
            self.BTN6.setText(answers[i][5])
            self.BTN1.show()
            self.BTN2.show()
            self.BTN3.show()
            self.BTN4.show()
            self.BTN5.show()
            self.BTN6.show()
        if n == 7:
            self.BTN1.setText(answers[i][0])
            self.BTN2.setText(answers[i][1])
            self.BTN3.setText(answers[i][2])
            self.BTN4.setText(answers[i][3])
            self.BTN5.setText(answers[i][4])
            self.BTN6.setText(answers[i][5])
            self.BTN7.setText(answers[i][5])
            self.BTN7.show()
            self.BTN1.show()
            self.BTN2.show()
            self.BTN3.show()
            self.BTN4.show()
            self.BTN5.show()
            self.BTN6.show()
        if n == 8:
            self.BTN1.setText(answers[i][0])
            self.BTN2.setText(answers[i][1])
            self.BTN3.setText(answers[i][2])
            self.BTN4.setText(answers[i][3])
            self.BTN5.setText(answers[i][4])
            self.BTN6.setText(answers[i][5])
            self.BTN7.setText(answers[i][5])
            self.BTN8.setText(answers[i][5])
            self.BTN8.show()
            self.BTN7.show()
            self.BTN1.show()
            self.BTN2.show()
            self.BTN3.show()
            self.BTN4.show()
            self.BTN5.show()
            self.BTN6.show()

    #선택한 항목의 결과값을 저장하는 함수
    def addAns1(self):
        YourAnswer[i][1] = 1
    def addAns2(self):
        YourAnswer[i][2] = 1
    def addAns3(self):
        YourAnswer[i][3] = 1
    def addAns4(self):
        YourAnswer[i][4] = 1
    def addAns5(self):
        YourAnswer[i][5] = 1
    def addAns6(self):
        YourAnswer[i][6] = 1
    def addAns7(self):
        YourAnswer[i][7] = 1
    def addAns8(self):
        YourAnswer[i][8] = 1

    #일단 고정질문 먼저할것임
    #뒤로가기, 대답 리스트에서 마지막 대답 지우기
    def goBack(self):
        global i, YourAnswer
        # 대답 항목 지우기
        for j in range(10):
            YourAnswer[i][j] = 0

        print(YourAnswer)

        #설문 화면 뒤로가기
        i = i-1
        if i < 0:
            i = 0
        else:
            i = i % 5
        self.hideAll()
        self.main()
        self.showQs()


    # 설문 화면 다음으로 넘기기(나중에 결과화면으로 넘겨야함)
    def goNext(self):
        global i
        i = i+1
        if i < 5:
            self.hideAll()
            self.main()
            self.showQs()
            print(YourAnswer)
        else:
            self.Questions.setText("결과화면")
            self.hideAll()
            print(YourAnswer)



app = QApplication()
win = My_window()

#임시
bar = win.statusBar()
bar.showMessage("임시 설문 창 입니다")
#임시

win.show()
app.exec()
