from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget

# AddressBook 클래스는 주소록 애플리케이션의 GUI를 정의하는 클래스입니다.
class AddressBook(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()  # UI를 초기화하는 함수 호출
        self.contacts = {}  # 연락처를 저장할 빈 딕셔너리 생성 (이름:전화번호 형식)

    # UI 구성 함수: 여기서 창에 들어갈 위젯을 배치합니다.
    def initUI(self):
        layout = QVBoxLayout()  # 세로 방향으로 위젯을 배치하는 레이아웃 객체 생성
        
        # 이름 입력 필드: 사용자가 이름을 입력할 수 있는 텍스트 박스
        self.name_input = QLineEdit(self)  # QLineEdit은 사용자가 텍스트를 입력할 수 있는 위젯
        self.name_input.setPlaceholderText("이름 입력")  # 입력 필드에 placeholder 텍스트 설정
        layout.addWidget(self.name_input)  # 레이아웃에 name_input 위젯 추가
        
        # 전화번호 입력 필드: 사용자가 전화번호를 입력할 수 있는 텍스트 박스
        self.phone_input = QLineEdit(self)  # 전화번호 입력 필드도 QLineEdit 위젯
        self.phone_input.setPlaceholderText("전화번호 입력")  # 전화번호 입력 필드에 placeholder 텍스트 설정
        layout.addWidget(self.phone_input)  # 레이아웃에 phone_input 위젯 추가
        
        # 저장 버튼: 연락처를 저장하는 버튼
        self.add_button = QPushButton("저장", self)  # 버튼 생성
        self.add_button.clicked.connect(self.add_contact)  # 버튼 클릭 시 add_contact 함수 연결
        layout.addWidget(self.add_button)  # 레이아웃에 add_button 위젯 추가
        
        # 검색 입력 필드: 사용자가 검색할 이름을 입력할 수 있는 텍스트 박스
        self.search_input = QLineEdit(self)  # 검색할 이름을 입력하는 텍스트 박스
        self.search_input.setPlaceholderText("검색할 이름 입력")  # 입력 필드에 placeholder 텍스트 설정
        layout.addWidget(self.search_input)  # 레이아웃에 search_input 위젯 추가
        
        # 검색 버튼: 사용자가 입력한 이름을 검색하는 버튼
        self.search_button = QPushButton("검색", self)  # 버튼 생성
        self.search_button.clicked.connect(self.search_contact)  # 버튼 클릭 시 search_contact 함수 연결
        layout.addWidget(self.search_button)  # 레이아웃에 search_button 위젯 추가
        
        # 결과 표시 리스트: 검색 결과를 보여주는 리스트 위젯
        self.result_list = QListWidget(self)  # 리스트 형태로 결과를 보여주는 위젯
        layout.addWidget(self.result_list)  # 레이아웃에 result_list 위젯 추가
        
        self.setLayout(layout)  # 최종적으로 설정한 레이아웃을 창에 적용
        self.setWindowTitle("주소록")  # 창 제목 설정
        self.setGeometry(300, 300, 300, 400)  # 창의 위치와 크기 설정 (x, y, width, height)
        
    # 연락처를 추가하는 함수
    def add_contact(self):
        # 사용자가 입력한 이름과 전화번호를 가져옵니다.
        name = self.name_input.text().strip()  # 이름 입력 필드에서 텍스트를 가져오고 앞뒤 공백을 제거
        phone = self.phone_input.text().strip()  # 전화번호 입력 필드에서 텍스트를 가져오고 앞뒤 공백을 제거
        
        # 이름과 전화번호가 모두 입력되었을 경우에만 연락처를 저장합니다.
        if name and phone:
            self.contacts[name] = phone  # 딕셔너리에 이름과 전화번호를 저장
            self.name_input.clear()  # 이름 입력 필드를 비웁니다.
            self.phone_input.clear()  # 전화번호 입력 필드를 비웁니다.
    
    # 검색 기능을 처리하는 함수
    def search_contact(self):
        # 사용자가 검색할 이름을 입력 필드에서 가져옵니다.
        search_name = self.search_input.text().strip()  # 검색할 이름을 입력 필드에서 가져오고 공백 제거
        self.result_list.clear()  # 이전 검색 결과를 지웁니다.
        
        # 연락처에 해당 이름이 있을 경우, 결과를 리스트에 추가합니다.
        if search_name in self.contacts:
            # 결과 리스트에 "이름: 전화번호" 형식으로 출력합니다.
            self.result_list.addItem(f"{search_name}: {self.contacts[search_name]}")
        else:
            # 결과가 없으면 "검색 결과 없음"을 리스트에 추가합니다.
            self.result_list.addItem("검색 결과 없음")

# 프로그램의 실행 시작점
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)  # 애플리케이션 객체 생성
    window = AddressBook()  # AddressBook 클래스의 객체 생성
    window.show()  # 생성한 창을 화면에 표시
    sys.exit(app.exec_())  # 이벤트 루프 시작, 프로그램 종료 시까지 대기
