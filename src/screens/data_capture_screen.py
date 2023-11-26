from ..shared.base_screen import *


class DataCaptureScreen(BaseScreen):
    def __init__(self, *args):
        super().__init__(*args)

        self.data_text = QLabel("Data", self)
        self.data_text.setObjectName("data_text")
        self.data_text.setFixedSize(40, 19)
        self.data_text.move(30, 35)

        self.data_text2 = QLabel("Capture", self)
        self.data_text2.setObjectName("data_text")
        self.data_text2.setFixedSize(70, 19)
        self.data_text2.move(30, 55)

        self.image_label = QLabel(self)
        self.image_label.setObjectName("image_label")
        pixmap = get_rounded_image()
        self.image_label.setPixmap(pixmap)
        self.image_label.setFixedSize(pixmap.size())
        self.image_label.move(250, 38)

        self.matric_no = QLineEdit("Matric NO", self)
        self.matric_no.setFixedSize(259, 43)
        self.matric_no.move(31, 132)

        self.name = QLineEdit("Name", self)
        self.name.setFixedSize(259, 43)
        self.name.move(31, 193)

        self.dept = QLineEdit("Department", self)
        self.dept.setFixedSize(259, 43)
        self.dept.move(31, 256)

        self.capture_finger_button = QPushButton("Capture Fingerprint", self)
        self.capture_finger_button.setObjectName("action")
        self.capture_finger_button.setFixedSize(260, 50)
        self.capture_finger_button.move(33, 345)
        self.capture_finger_button.clicked.connect(
            self.eduttend.showFingerprinCaptureScreen
        )

        self.capture_face_button = QPushButton("Capture Face", self)
        self.capture_face_button.setObjectName("action")
        self.capture_face_button.setFixedSize(260, 50)
        self.capture_face_button.move(33, 405)
        self.capture_face_button.clicked.connect(self.eduttend.showFaceIDCaptureScreen)
