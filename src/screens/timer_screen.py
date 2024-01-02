from ..shared.base_screen import *


class TimerScreen(BaseScreen):
    def __init__(self, *args):
        super().__init__(*args)

        self.timer_text = QLabel("Set", self)
        self.timer_text.setObjectName("bold_text")
        self.timer_text.setFixedSize(26, 20)
        self.timer_text.move(30, 35)

        self.timer_text = QLabel("Timer", self)
        self.timer_text.setObjectName("bold_text")
        self.timer_text.setFixedSize(48, 19)
        self.timer_text.move(30, 55)

        self.image_label = QLabel(self)
        self.image_label.setObjectName("image_label")
        # pixmap = get_rounded_image()
        # self.image_label.setPixmap(pixmap)
        # self.image_label.setFixedSize(pixmap.size())
        self.image_label.move(250, 35)

        self.time = None

        self.time15 = QPushButton("15 mins", self)
        self.time15.setObjectName("countdown_time")
        self.time15.setFixedSize(100, 50)
        self.time15.move(111, 100)
        self.time15.clicked.connect(lambda: self.set_time(15))
        self.time15.setAutoExclusive(True)
        self.time15.setCheckable(True)

        self.time30 = QPushButton("30 mins", self)
        self.time30.setObjectName("countdown_time")
        self.time30.setFixedSize(100, 50)
        self.time30.move(111, 170)
        self.time30.clicked.connect(lambda: self.set_time(45))
        self.time30.setAutoExclusive(True)
        self.time30.setCheckable(True)

        self.time45 = QPushButton("45 mins", self)
        self.time45.setObjectName("countdown_time")
        self.time45.setFixedSize(100, 50)
        self.time45.move(111, 240)
        self.time45.clicked.connect(lambda: self.set_time(45))
        self.time45.setAutoExclusive(True)
        self.time45.setCheckable(True)

        self.no_time = QPushButton("No Timer", self)
        self.no_time.setObjectName("countdown_time")
        self.no_time.setFixedSize(100, 50)
        self.no_time.move(111, 310)
        self.no_time.clicked.connect(lambda: self.set_time(0))
        self.no_time.setAutoExclusive(True)
        self.no_time.setCheckable(True)

        self.set_timer_button = QPushButton("Set Timer", self)
        self.set_timer_button.setObjectName("action")
        self.set_timer_button.setFixedSize(260, 50)
        self.set_timer_button.move(30, 382)
        self.set_timer_button.clicked.connect(self.set_timer)
        # self.set_timer_button.clicked.connect(self.eduttend.showChooseAttendanceScreen)

    def set_time(self, time: int):
        self.time = time

    def set_timer(self):
        if self.time != None:
            self.eduttend.showFaceIDFeedbackScreen(self.time)
        else:
            QMessageBox.critical(self, "Invalid Time", "Choose a timer")
