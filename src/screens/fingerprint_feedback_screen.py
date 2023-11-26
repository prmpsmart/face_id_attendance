from ..shared.base_screen import *


class FingerprintFeedbackScreen(BaseScreen):
    def __init__(self, *args):
        super().__init__(*args)

        self.ff_text = QLabel("Timer", self)
        self.ff_text.setObjectName("ff_text")
        self.ff_text.setFixedSize(35, 14)
        self.ff_text.move(30, 35)

        self.ff_text2 = QLabel("Countdown", self)
        self.ff_text2.setObjectName("ff_text")
        self.ff_text2.setFixedSize(70, 14)
        self.ff_text2.move(30, 53)

        self.ff_text3 = QLabel("08:00:05", self)
        self.ff_text3.setObjectName("ff_text3")
        self.ff_text3.setFixedSize(80, 23)
        self.ff_text3.move(30, 71)

        self.image_label = QLabel(self)
        self.image_label.setObjectName("image_label")
        pixmap = get_rounded_image()
        self.image_label.setPixmap(pixmap)
        self.image_label.setFixedSize(pixmap.size())
        self.image_label.move(250, 38)

        self.ff_text4 = QLabel("Please scan fingerprint", self)
        self.ff_text4.setObjectName("ff_text4")
        self.ff_text4.setFixedSize(167, 19)
        self.ff_text4.move(84, 153)

        self.image_label = QLabel(self)
        pixmap = QPixmap(":/fingerprint").scaled(100, 100)
        self.image_label.setPixmap(pixmap)
        self.image_label.setFixedSize(pixmap.size())
        self.image_label.move(110, 190)

        self.ff_text5 = QLabel("Matric NO", self)
        self.ff_text5.setObjectName("ff_text4")
        self.ff_text5.setFixedSize(75, 19)
        self.ff_text5.move(127, 332)

        self.notify = Notify(self)
        self.notify.setFixedSize(191, 68)
        self.notify.move(68, 369)

        self.hide_time = 2000

    def showEvent(self, e):
        QTimer.singleShot(self.hide_time, self.show_accepted)

    def show_accepted(self):
        self.notify.show_accepted()
        QTimer.singleShot(self.hide_time, self.show_rejected)

    def show_rejected(self):
        self.notify.show_rejected()
        QTimer.singleShot(self.hide_time, self.show_not_registered)

    def show_not_registered(self):
        self.notify.show_not_registered()
        QTimer.singleShot(self.hide_time, self.eduttend.showChooseAttendanceScreen)
