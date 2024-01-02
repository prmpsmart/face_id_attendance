from ..shared.base_screen import *
from ..shared.cam_screen import CamScreen
from ..shared.spinner import PRMP_QSpinner


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

        # self.capture_face_button = QPushButton("Capture Face", self)
        self.capture_face_button = QPushButton("Login", self)
        self.capture_face_button.setObjectName("action")
        self.capture_face_button.setFixedSize(260, 50)
        self.capture_face_button.move(33, 375)
        self.capture_face_button.clicked.connect(self.make_request)

        self.spiner = PRMP_QSpinner(self, disableParentWhenSpinning=True)

    def make_request(self):
        self.camera.stop()
        self.spiner.start()
        return super().make_request(1000)

    def on_request_timeout(self):
        self.spiner.stop()
        self.eduttend.showApprovedScreen(Profile(self.camera.image))
        # self.eduttend.showDenyScreen()
        return super().on_request_timeout()
