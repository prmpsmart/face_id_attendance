from typing import Callable
from .commons import *
from PySide6.QtMultimedia import *
from PySide6.QtMultimediaWidgets import *


class Camera:
    def __init__(
        self,
        receiver: Callable[[QImage], None] = None,
        fps: int = 24,
        camera_device: QCameraDevice = None,
        mirror: bool = False,
    ):
        self.receiver = receiver
        self.fps = fps
        self.mirror = mirror

        self.timer = QTimer()
        self.timer.timeout.connect(self.capture)
        self.camera: QCamera = None

        if camera_device:
            self.setup_camera(camera_device)

    def capture(self):
        if self.image_capture:
            self.image_capture.capture()

    def setup_camera(self, camera_device: QCameraDevice):
        self.camera_device = camera_device
        self.camera = QCamera(self.camera_device)

        self.image_capture = QImageCapture(self.camera)
        self.image_capture.imageCaptured.connect(self.image_captured)
        self.image_capture.errorOccurred.connect(self.capture_error)

        self.capture_session = QMediaCaptureSession()
        self.capture_session.setCamera(self.camera)
        self.capture_session.setImageCapture(self.image_capture)

    def set_fps(self, fps):
        if fps:
            self.timer.setInterval(1000 / fps)

    def image_captured(self, id: int, image: QImage):
        image = image.convertToFormat(QImage.Format_ARGB32)

        if self.mirror:
            image.mirror(1, 0)

        if self.receiver:
            self.receiver(image)

    def start(self):
        if self.camera:
            self.camera.start()
            self.timer.start()

    def stop(self):
        if self.camera:
            self.camera.stop()
        self.timer.stop()

    def isActive(self):
        if self.camera:
            return self.camera.isActive()

    def show_status_message(self, message):
        # print(message)
        ...

    def capture_error(self, id: int, error: QImageCapture.Error, error_string: str):
        self.show_status_message(error_string)


class CameraWidget(QLabel):
    def __init__(
        self,
        fps: int = 50,
        start: bool = False,
        output: bool = False,
        receiver: Callable[[QImage], None] = None,
        camera_device: QCameraDevice = None,
        mirror: bool = True,
        **kwargs
    ):
        super().__init__(**kwargs)

        self.output = output
        self.receiver = receiver

        self.camera = Camera(
            self.image_captured,
            fps=fps,
            mirror=mirror,
            camera_device=camera_device,
        )

        self.image: QImage = None

        if start:
            self.start()

    def set_camera(self, camera_device: QCameraDevice):
        self.camera.setup_camera(camera_device)

    def image_captured(self, image: QImage):
        image = image.scaled(
            self.size(),
            Qt.AspectRatioMode.IgnoreAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

        self.image = image
        if self.output:
            self.setPixmap(QPixmap(image))

        if self.receiver:
            self.receiver(image)

    def set_fps(self, fps: int):
        self.camera.set_fps(fps)

    def start(self):
        self.camera.start()

    def toggle(self):
        if self.camera.isActive():
            self.camera.stop()
        else:
            self.camera.start()

    def stop(self):
        self.camera.stop()

    def closeEvent(self, event: QCloseEvent):
        self.camera.stop()
        event.accept()
