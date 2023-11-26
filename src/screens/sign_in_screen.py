from ..shared.base_screen import *


class SignInScreen(BaseScreen):
    def __init__(self, *args):
        super().__init__(*args)

        self.signin_text = QLabel("Sign In using", self)
        self.signin_text.setObjectName("signin_text")
        self.signin_text.setFixedSize(118, 23)
        self.signin_text.move(101, 135)

        self.fingerprint_button = QPushButton(
            QIcon(":/fingerprint"), "  Fingerprint", self
        )
        self.fingerprint_button.setIconSize(QSizeF(51.74, 40).toSize())
        self.fingerprint_button.setFixedSize(260, 60)
        self.fingerprint_button.move(30, 203)
        self.fingerprint_button.setObjectName("choose")
        self.fingerprint_button.clicked.connect(
            self.eduttend.showFingerprintLoginScreen
        )

        effect = QGraphicsDropShadowEffect()
        effect.setOffset(0, 3)
        self.fingerprint_button.setGraphicsEffect(effect)

        self.face_id_button = QPushButton(QIcon(":/face"), "  Face ID", self)
        self.face_id_button.setIconSize(QSizeF(51.74, 40).toSize())
        self.face_id_button.setFixedSize(260, 60)
        self.face_id_button.setObjectName("choose")
        self.face_id_button.move(30, 284)
        self.face_id_button.clicked.connect(self.eduttend.showFaceIDLoginScreen)

        effect = QGraphicsDropShadowEffect()
        effect.setOffset(0, 3)
        self.face_id_button.setGraphicsEffect(effect)
