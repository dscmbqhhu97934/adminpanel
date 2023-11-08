from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import server
import time
import Anim
import sys

print("success import UI lib")

anim_data = [255,250]


class login(QMainWindow):
    def __init__(self):
        super().__init__()

        self._startPos = None
        self._endPos = None
        self._tracking = False

        # Reset Window Size
        self.resize(750, 550)

        # Set Window Background
        self.centralwidget = QWidget(self)
        self.centralwidget.resize(750, 550)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        radius = 15
        self.centralwidget.setStyleSheet(
            """
            background:rgb(30,30,61);
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;
            """.format(radius)
        )

        self.login_ui_list = {}
        self.draw = {}

        self.initUI()

    def initUI(self):
        # Render
        self.Render()

        # Show
        self.center()
        self.show()

    def Render(self):
        def status():
            self.statusbar = QWidget(self)
            self.statusbar.resize(750, 30)

            self.statusbar.move(0, 520)

            self.statusbar.setStyleSheet(
                """
                background:rgb(25,25,54);
                border-bottom-left-radius:{0}px;
                border-bottom-right-radius:{0}px;
                """.format(15)
            )

            return_message = server.connect_to_server(True, "1")
            lbl1 = QLabel(return_message["Message"], self)
            lbl1.setStyleSheet("""
            color:rgb(103,105,143);
            """)
            lbl1.setFont(QFont('猫啃珠圆体', 7))
            lbl1.move(12, 525)
            lbl1.setAlignment(Qt.AlignCenter)

            lbl2 = QLabel("H1wks Panel", self)
            lbl2.setStyleSheet("""
                        color:rgb(103,105,143);
                        """)
            lbl2.setFont(QFont('猫啃珠圆体', 7))
            lbl2.move(645, 522)
            lbl2.setAlignment(Qt.AlignCenter)

            lbl1.adjustSize()

        def Main_text():
            self.statusbar = QWidget(self)
            self.statusbar.resize(450, 70)

            self.statusbar.move(150, 70)

            self.statusbar.setStyleSheet(
                """
                background:rgb(38,38,76);

                border-top-left-radius:{0}px;
                border-bottom-left-radius:{0}px;
                border-top-right-radius:{0}px;
                border-bottom-right-radius:{0}px;
                """.format(15)
            )

            lbl1 = QLabel('H1wks ADMIN Panel', self)
            lbl1.setStyleSheet("""
                color:rgb(234,234,245);
            """)
            lbl1.setFont(QFont('猫啃珠圆体', 17))
            lbl1.move(200, 85)
            lbl1.setAlignment(Qt.AlignCenter)

            lbl1.adjustSize()

        def ui_objects():

            # Username
            self.login_ui_list["username_input"] = QLineEdit(self)
            self.login_ui_list["username_input"].setPlaceholderText('username')
            self.login_ui_list["username_input"].setFont(QFont('猫啃珠圆体', 7))
            self.login_ui_list["username_input"].move(200, 200)
            self.login_ui_list["username_input"].resize(350, 50)
            self.login_ui_list["username_input"].setStyleSheet("""
                background: rgba(38,38,76,255);
                color:#fff;
                padding-left: 20px;
                margin-right: 1px;
                border-radius:8px;
            """)
            self.login_ui_list["username_label"] = QLabel("username", self)
            self.login_ui_list["username_label"].setFont(QFont('猫啃珠圆体', 7))
            self.login_ui_list["username_label"].move(215, 177)
            self.login_ui_list["username_label"].setStyleSheet("""
                color:rgba(234,234,245,255);
            """)

            # Password
            self.login_ui_list["password_input"] = QLineEdit(self)
            self.login_ui_list["password_input"].setPlaceholderText('password')
            self.login_ui_list["password_input"].setFont(QFont('猫啃珠圆体', 7))
            self.login_ui_list["password_input"].move(200, 285)
            self.login_ui_list["password_input"].resize(350, 50)
            self.login_ui_list["password_input"].setEchoMode(QLineEdit.Password)
            self.login_ui_list["password_input"].setStyleSheet("""
                background: rgba(38,38,76,255);
                color:#fff;
                padding-left: 20px;
                margin-right: 1px;
                border-radius:8px;
            """)
            self.login_ui_list["password_label"] = QLabel("password", self)
            self.login_ui_list["password_label"].setFont(QFont('猫啃珠圆体', 7))
            self.login_ui_list["password_label"].move(215, 262)
            self.login_ui_list["password_label"].setStyleSheet("""
                color:rgba(234,234,245,255);
            """)

            # Login Button
            self.login_ui_list["login_button"] = QPushButton('Login', self)
            self.login_ui_list["login_button"].setFont(QFont('猫啃珠圆体', 7))
            self.login_ui_list["login_button"].move(250, 370)
            self.login_ui_list["login_button"].resize(250, 50)
            self.login_ui_list["login_button"].setStyleSheet("""
                background: rgba(255,93,171,255);
                color:#fff;
                border-top-left-radius:15px;
                border-bottom-left-radius:8px;
                border-top-right-radius:8px;    
                border-bottom-right-radius:15px;
            """)
            

            def logining():
                self.login_hide_ctrl(show=False)
                server.connect_to_server(False, [self.login_ui_list["username_input"].text(), self.login_ui_list["password_input"].text()])

            self.login_ui_list["login_button"].clicked.connect(logining)

        def quit_btn():
            #render circle
            self.quit_btn = QPushButton(self)
            self.quit_btn.move(730, 10)
            self.quit_btn.resize(14, 14)
            self.quit_btn.setStyleSheet("""
                background: rgb(255,93,171);
                border-radius:7px;
            """)
            self.quit_btn.clicked.connect(self.close)

        def min_btn():
            self.min_btn = QPushButton(self)
            self.min_btn.move(710, 10)
            self.min_btn.resize(14, 14)
            self.min_btn.setStyleSheet("""
                background: rgb(240,230,140);
                border-radius:7px;
            """)
            self.min_btn.clicked.connect(self.showMinimized)

        min_btn()
        quit_btn()
        ui_objects()
        status()
        Main_text()

    def login_hide_ctrl(self, show):
        if show:
            while anim_data[1] <= 250:
                anim_data[1] = anim_data[1] + 50
                
                self.login_ui_list["username_input"].setStyleSheet("""
                    background: rgba(38,38,76, {0});
                    color:rgba(255,255,255, {0});
                    padding-left: 20px;
                    margin-right: 1px;
                    border-radius:8px;
                """.format(anim_data[1]))
                self.login_ui_list["password_input"].setStyleSheet("""
                    background: rgba(38,38,76, {0});
                    color:rgba(255,255,255,{0});
                    padding-left: 20px;
                    margin-right: 1px;
                    border-radius:8px;
                """.format(anim_data[1]))
                self.login_ui_list["username_label"].setStyleSheet("""
                    color:rgba(234,234,245, {0});
                """.format(anim_data[1]))
                self.login_ui_list["password_label"].setStyleSheet("""
                    color:rgba(234,234,245, {0});
                """.format(anim_data[1]))
                self.login_ui_list["login_button"].setStyleSheet("""
                    background: rgba(255,93,171,{0});
                    color: rgba(255,255,255,{0});
                    border-top-left-radius:15px;
                    border-bottom-left-radius:8px;
                    border-top-right-radius:8px;
                    border-bottom-right-radius:15px;
                """.format(anim_data[1]))
                self.login_ui_list["login_button"].repaint()
                self.login_ui_list["username_input"].repaint()
                self.login_ui_list["password_input"].repaint()
                self.login_ui_list["username_label"].repaint()
                self.login_ui_list["password_label"].repaint()
                self.login_ui_list["login_button"].repaint()

                QApplication.processEvents()
                time.sleep(0.05)
            self.login_ui_list["password_input"].hide()
            self.login_ui_list["username_input"].hide()
        else:
            while anim_data[1] > 0:
                anim_data[1] = anim_data[1] - 50
                
                self.login_ui_list["username_input"].setStyleSheet("""
                    background: rgba(38,38,76, {0});
                    color:rgba(255,255,255, {0});
                    padding-left: 20px;
                    margin-right: 1px;
                    border-radius:8px;
                """.format(anim_data[1]))
                self.login_ui_list["password_input"].setStyleSheet("""
                    background: rgba(38,38,76, {0});
                    color:rgba(255,255,255,{0});
                    padding-left: 20px;
                    margin-right: 1px;
                    border-radius:8px;
                """.format(anim_data[1]))
                self.login_ui_list["username_label"].setStyleSheet("""
                    color:rgba(234,234,245, {0});
                """.format(anim_data[1]))
                self.login_ui_list["password_label"].setStyleSheet("""
                    color:rgba(234,234,245, {0});
                """.format(anim_data[1]))
                self.login_ui_list["login_button"].setStyleSheet("""
                    background: rgba(255,93,171,{0});
                    color: rgba(255,255,255,{0});
                    border-top-left-radius:15px;
                    border-bottom-left-radius:8px;
                    border-top-right-radius:8px;
                    border-bottom-right-radius:15px;
                """.format(anim_data[1]))
                self.login_ui_list["login_button"].repaint()
                self.login_ui_list["username_input"].repaint()
                self.login_ui_list["password_input"].repaint()
                self.login_ui_list["username_label"].repaint()
                self.login_ui_list["password_label"].repaint()
                self.login_ui_list["login_button"].repaint()

                QApplication.processEvents()
                time.sleep(0.05)
            self.login_ui_list["password_input"].hide()
            self.login_ui_list["username_input"].hide()

        print("123")

    def center(self):
        qr = self.frameGeometry()
        qr.moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(qr.topLeft())

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None

    def quit(self):
        self.close()

    def min(self):
        self.showMinimized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = login()
    sys.exit(app.exec_())
