from ..shared.base_screen import *


class DenyScreen(BaseScreen):
    def __init__(self, *args):
        super().__init__(*args)

        self.image_label = QLabel(self)
        pixmap = QPixmap(":/cancel").scaled(100, 100)
        self.image_label.setPixmap(pixmap)
        self.image_label.setFixedSize(pixmap.size())
        self.image_label.move(110, 151)

        self.deny_text_red = QLabel("Login", self)
        self.deny_text_red.setObjectName("deny_text_red")
        self.deny_text_red.setFixedSize(65, 26)
        self.deny_text_red.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.deny_text_red.move(128, 279)

        self.deny_text_red2 = QLabel("Failed!!!", self)
        self.deny_text_red2.setObjectName("deny_text_red")
        self.deny_text_red2.setFixedSize(147, 31)
        self.deny_text_red2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.deny_text_red2.move(87, 305)

        self.deny_text = QLabel("Try:", self)
        self.deny_text.setObjectName("deny_text")
        self.deny_text.setFixedSize(25, 17)
        self.deny_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.deny_text.move(150, 349)

        self.deny_text2 = QLabel("Placing your finger and face well", self)
        self.deny_text2.setObjectName("deny_text")
        self.deny_text2.setFixedSize(185, 16)
        self.deny_text2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.deny_text2.move(68, 363)

        self.deny_text3 = QLabel("Creating an account", self)
        self.deny_text3.setObjectName("deny_text")
        self.deny_text3.setFixedSize(115, 14)
        self.deny_text3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.deny_text3.move(103, 379)

    def showEvent(self, e):
        QTimer.singleShot(
            1000,
            self.eduttend.showApprovedScreen,
        )
