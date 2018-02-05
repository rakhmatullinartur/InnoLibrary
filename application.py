import sys
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout, QLabel, QLineEdit, QMainWindow, QAction, qApp, QDesktopWidget, QWidget, QMessageBox, QApplication



class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    width, height = 350, 300
    book_names = ['ItP', 'Algorithms']
    # positions = [(50, 50), (100, 100)]


    def initUI(self):

        login = QLabel('Login')
        password = QLabel('Password')
        self.logEdit = QLineEdit()
        self.passEdit = QLineEdit()
        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.grid.addWidget(login, 1, 0)
        self.grid.addWidget(self.logEdit, 1, 1)
        self.grid.addWidget(password, 2, 0)
        self.grid.addWidget(self.passEdit, 2, 1)
        self.setLayout(self.grid)

        self.loginBtn = QPushButton('Log In!', self)
        self.loginBtn.move(150, 250)
        self.signUpBtn = QPushButton('Sign up?', self)
        self.signUpBtn.move(250, 250)
        self.signUpBtn.clicked.connect(self.userSignUp)
        self.loginBtn.clicked.connect(self.userLogIn)

        # exitAction = QAction('&Exit', self)
        # exitAction.setShortcut('Ctrl+Q')
        # exitAction.triggered.connect(qApp.quit)
        # self.statusBar()
        # menubar = self.menuBar()
        # fileMenu = menubar.addMenu('&File')
        # fileMenu.addAction(exitAction)

        self.resize(self.width, self.height)
        self.center()
        self.setWindowTitle('Quit Button')
        self.show()

    def userLogIn(self):
        print(self.logEdit.text())

    def userSignUp(self):
        self.loginBtn.deleteLater()
        self.signUpBtn.deleteLater()
        self.clearLayout(self.grid)
        self.resize(500, 450)
        self.placeBooks()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def placeBooks(self):
        self.positions = [(x, y) for x in range(self.width) for y in range(self.height)]
        for position, name in zip(self.positions, self.book_names):
            button = QPushButton(name, self)
            self.grid.addWidget(button, *position)
            button.clicked.connect(self.showBook)

    def showBook(self):
        sender = self.sender()
        print(sender.text())
        self.clearLayout(self.grid)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are You sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def clearLayout(self, layout):
        for i in range(layout.count()):
            layout.itemAt(i).widget().close()

        print('test')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())