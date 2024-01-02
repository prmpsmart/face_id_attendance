from .base_screen import *
from .cam6 import CameraWidget, QMediaDevices, QCameraDevice


class CamScreen(BaseScreen):
    def __init__(
        self,
        *args,
        scale=(370, 308),
        move=(-25, -15),
        margin=(50, 10),
    ):
        super().__init__(*args)

        self.image_label = QLabel(self)
        pixmap = QPixmap(":/frame").scaled(*scale)
        self.image_label.setPixmap(pixmap)
        self.image_label.setFixedSize(pixmap.size())
        self.image_label.move(*move)

        lay = QVBoxLayout(self.image_label)
        m, b = margin
        lay.setContentsMargins(m, m - b, m, m - b)

        self.available_cameras = QMediaDevices.videoInputs()

        self.camera = CameraWidget(
            camera_device=self.available_cameras[0],
            output=True,
            receiver=self.image_receiver,
        )
        self.camera.start()
        lay.addWidget(self.camera)

        # self.capture_face_button = QPushButton("Capture Face", self)
        # self.capture_face_button.setObjectName("action")
        # self.capture_face_button.setFixedSize(260, 50)
        # self.capture_face_button.move(33, 375)
        # self.capture_face_button.clicked.connect(self.showCapture)

        self.buttons_widget = QWidget(self)
        self.buttons_widget.setFixedWidth(280)
        self.buttons_widget.move(20, 430)

        self.hlay = QHBoxLayout(self.buttons_widget)

        for cam in self.available_cameras:
            button = PushButton(cam, self)
            self.hlay.addWidget(button)

    def image_receiver(self, image: QImage):
        ...

    def set_camera(self, camera_device: QCameraDevice):
        self.camera.set_camera(camera_device)
        self.camera.start()

    # def showCapture(self, e):
    #     self.camera.stop()
    #     self.eduttend.showFaceIDCaptureScreen()


class PushButton(QPushButton):
    def __init__(self, camera_device: QCameraDevice, parent: CamScreen):
        super().__init__(camera_device.description())
        self.win = parent
        self.camera_device = camera_device
        self.toggled.connect(self.push)
        self.setAutoExclusive(True)
        self.setCheckable(True)

    def push(self, toggled: bool):
        if toggled:
            self.win.set_camera(self.camera_device)
