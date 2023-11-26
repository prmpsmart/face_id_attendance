from ..shared.base_screen import *
from ..shared.cam_screen import CamScreen


class FaceIDLoginScreen(CamScreen):
    def __init__(self, *args):
        super().__init__(
            *args,
            scale=(370, 308),
            move=(-25, -15),
            margin=(50, 10),
        )

        self.face_id_login_text = QLabel("Let the camera", self)
        self.face_id_login_text.setObjectName("face_id_login_text")
        self.face_id_login_text.setFixedSize(200, 27)
        self.face_id_login_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.face_id_login_text.move(60, 288)

        self.face_id_login_text2 = QLabel("capture your face", self)
        self.face_id_login_text2.setObjectName("face_id_login_text")
        self.face_id_login_text2.setFixedSize(200, 27)
        self.face_id_login_text2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.face_id_login_text2.move(60, 325)

        self.capture_face_button = QPushButton("Capture Face", self)
        self.capture_face_button.setObjectName("action")
        self.capture_face_button.setFixedSize(260, 50)
        self.capture_face_button.move(33, 375)
        self.capture_face_button.clicked.connect(self.showCapture)

    def showCapture(self, e):
        if self.camera.camera.isActive():
            self.camera.stop()
        else:
            self.camera.start()
        self.eduttend.showDenyScreen()
