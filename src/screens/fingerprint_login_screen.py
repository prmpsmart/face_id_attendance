from ..shared.base_screen import *


class FingerprintLoginScreen(BaseScreen):
    def __init__(self, *args):
        super().__init__(*args)

        self.image_label = QLabel(self)
        pixmap = QPixmap(":/fingerprint").scaled(100, 100)
        self.image_label.setPixmap(pixmap)
        self.image_label.setFixedSize(pixmap.size())
        self.image_label.move(110, 130)

        self.fingerprint_login_text = QLabel("Place your finger on", self)
        self.fingerprint_login_text.setObjectName("fingerprint_login_text")
        self.fingerprint_login_text.setFixedSize(197, 23)
        self.fingerprint_login_text.move(62, 266)

        self.fingerprint_login_text2 = QLabel("the sensor", self)
        self.fingerprint_login_text2.setObjectName("fingerprint_login_text")
        self.fingerprint_login_text2.setFixedSize(197, 23)
        self.fingerprint_login_text2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fingerprint_login_text2.move(61, 298)

    def showEvent(self, e):
        QTimer.singleShot(
            1000,
            self.eduttend.showDenyScreen,
        )
