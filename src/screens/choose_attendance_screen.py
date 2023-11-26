from ..shared.base_screen import *


class ChooseAttendanceScreen(BaseScreen):
    def __init__(self, *args):
        super().__init__(*args)

        self.take_text = QLabel("Take Attendance using", self)
        self.take_text.setObjectName("take_text")
        self.take_text.setFixedSize(155, 48)
        self.take_text.move(83, 135)
        self.take_text.setWordWrap(True)
        self.take_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.fingerprint_button = QPushButton(
            QIcon(":/fingerprint"), "  Fingerprint", self
        )
        self.fingerprint_button.setIconSize(QSizeF(51.74, 40).toSize())
        self.fingerprint_button.setFixedSize(260, 60)
        self.fingerprint_button.move(30, 203)
        self.fingerprint_button.setObjectName("choose")
        self.fingerprint_button.clicked.connect(
            self.eduttend.showFingerprintFeedbackScreen
        )

        effect = QGraphicsDropShadowEffect()
        effect.setOffset(0, 3)
        self.fingerprint_button.setGraphicsEffect(effect)

        self.face_id_button = QPushButton(QIcon(":/face"), "  Face ID", self)
        self.face_id_button.setIconSize(QSizeF(51.74, 40).toSize())
        self.face_id_button.setFixedSize(260, 60)
        self.face_id_button.move(30, 284)
        self.face_id_button.setObjectName("choose")
        self.face_id_button.clicked.connect(self.eduttend.showFaceIDFeedbackScreen)

        effect = QGraphicsDropShadowEffect()
        effect.setOffset(0, 3)
        self.face_id_button.setGraphicsEffect(effect)
