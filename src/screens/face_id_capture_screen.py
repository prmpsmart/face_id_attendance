from ..shared.base_screen import *
from ..shared.cam_screen import CamScreen


class FaceIDCaptureScreen(CamScreen):
    def __init__(self, *args):
        super().__init__(
            *args,
            scale=(370, 250),
            move=(-25, 102),
            margin=(50, 15),
        )
        # self.camera.output =0
        # self.camera.setStyleSheet('background:red')

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

        self.ff_text4 = QLabel("Place your face in the camera", self)
        self.ff_text4.setObjectName("ff_text4")
        self.ff_text4.setFixedSize(219, 19)
        self.ff_text4.move(50, 100)

        self.ff_text5 = QLabel("Matric NO", self)
        self.ff_text5.setObjectName("ff_text4")
        self.ff_text5.setFixedSize(75, 19)
        self.ff_text5.move(127, 332)

        self.notify = Notify(self)
        self.notify.setFixedSize(191, 68)
        self.notify.move(68, 369)

        self.hide_time = 1000

        
        self.capture_face_button = QPushButton("Capture Face", self)
        self.capture_face_button.setObjectName("action")
        self.capture_face_button.setFixedSize(260, 50)
        self.capture_face_button.move(33, 375)
        self.capture_face_button.clicked.connect(self.camera.toggle)

    # def showEvent(self, e):
    #     QTimer.singleShot(self.hide_time, self.show_captured)

    def show_captured(self):
        self.notify.show_captured()
        QTimer.singleShot(self.hide_time, self.show_rejected)

    def show_rejected(self):
        self.notify.show_rejected()
        QTimer.singleShot(self.hide_time, self.eduttend.showDataCaptureScreen)
