from ..shared.base_screen import *


class ApprovedScreen(BaseScreen):
    def __init__(self, *args):
        super().__init__(*args)

        self.image_label = QLabel(self)
        pixmap = QPixmap(":/check").scaled(100, 100)
        self.image_label.setPixmap(pixmap)
        self.image_label.setFixedSize(pixmap.size())
        self.image_label.move(111, 149)

        self.approved_text = QLabel("Login", self)
        self.approved_text.setObjectName("approved_text")
        self.approved_text.setFixedSize(200, 27)
        self.approved_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.approved_text.move(60, 280)

        self.approved_text2 = QLabel("Successful", self)
        self.approved_text2.setObjectName("approved_text")
        self.approved_text2.setFixedSize(147, 31)
        self.approved_text2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.approved_text2.move(86, 312)

    def showEvent(self, e):
        QTimer.singleShot(
            1000,
            self.eduttend.showHomeScreen,
        )
