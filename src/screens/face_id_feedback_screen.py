from src.shared.spinner import PRMP_QSpinner
from ..shared.cam_screen import *


class FaceIDFeedbackScreen(CamScreen):
    def __init__(self, *args, profile: Profile):
        super().__init__(
            *args,
            scale=(330, 288),
            move=(-5, 80),
            margin=(50, 10),
        )

        self.profile = profile

        self.ff_text = QLabel("Timer", self)
        self.ff_text.setObjectName("ff_text")
        self.ff_text.setFixedSize(35, 14)
        self.ff_text.move(30, 15)

        self.ff_text2 = QLabel("Countdown", self)
        self.ff_text2.setObjectName("ff_text")
        self.ff_text2.setFixedSize(70, 14)
        self.ff_text2.move(30, 35)

        self.ff_text3 = QLabel(f"00:{str(profile.time).zfill(2)}:00", self)
        self.ff_text3.setObjectName("ff_text3")
        self.ff_text3.setFixedSize(80, 23)
        self.ff_text3.move(30, 51)

        self.image_label = QLabel(self)
        self.image_label.setObjectName("image_label")
        pixmap = get_rounded_image(profile.image)
        self.image_label.setPixmap(pixmap)
        self.image_label.setFixedSize(pixmap.size())
        self.image_label.move(250, 8)

        self.ff_text4 = QLabel("Place your face in the camera", self)
        self.ff_text4.setObjectName("ff_text4")
        self.ff_text4.setFixedSize(219, 29)
        self.ff_text4.move(50, 80)

        self.ff_text5 = QLabel("Matric NO", self)
        self.ff_text5.setObjectName("ff_text4")
        self.ff_text5.setFixedSize(100, 19)
        self.ff_text5.move(120, 340)
        self.ff_text5.hide()

        self.capture_face_button = QPushButton("Capture", self)
        self.capture_face_button.setObjectName("action")
        self.capture_face_button.setFixedSize(260, 40)
        self.capture_face_button.move(30, 382)
        self.capture_face_button.clicked.connect(self.make_request)

        self.notify = Notify(self)
        self.notify.setFixedSize(191, 68)
        self.notify.move(68, 362)
        self.notify.hidden.connect(self.notify_hidden)

        self.count = 0

        self.spiner = PRMP_QSpinner(self, disableParentWhenSpinning=True)

        self.hlay.addStretch()
        # self.hlay.addSpacing(900)

        end_button = QPushButton("End Attendance", self)
        end_button.clicked.connect(self.end_attendance)
        self.hlay.addWidget(end_button)

        self.hide_time = 1000

        self.time = profile.time * 60
        if self.time:
            self.timer = QTimer()
            self.timer.setInterval(1000)
            self.timer.timeout.connect(self.update_time)

    def end_attendance(self):
        self.camera.stop()
        if self.time:
            self.timer.stop()
        self.eduttend.showWelcomeScreen()

    def make_request(self):
        self.camera.stop()
        self.spiner.start()
        self.capture_face_button.hide()
        return super().make_request(1500)

    def on_request_timeout(self):
        self.spiner.stop()
        self.notify.show_accepted(1500)

        self.ff_text5.setText("IPE/18/8560")
        self.ff_text5.show()

        QTimer.singleShot(
            1000, lambda: (self.ff_text5.hide(), self.notify.show_rejected())
        )

        QTimer.singleShot(4000, lambda: self.notify.show_not_registered(5000))
        # self.notify.show_rejected()
        # self.notify.show_not_registered()

        return super().on_request_timeout()

    def notify_hidden(self):
        self.count += 1
        if self.count > 1:
            self.camera.start()
            self.capture_face_button.show()
            self.ff_text5.hide()

    def showEvent(self, e):
        if self.time:
            self.timer.start()
        # QTimer.singleShot(self.hide_time, self.show_accepted)

    def update_time(self):
        self.time -= 1
        if not self.time:
            self.timer.stop()
            # navigate to the attendance closed page
        div, mod = divmod(self.time, 60)
        self.ff_text3.setText(f"00:{str(div).zfill(2)}:{mod}")
