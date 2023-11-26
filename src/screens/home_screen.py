from ..shared.base_screen import *


class HomeScreen(BaseScreen):
    def __init__(self, *args):
        super().__init__(*args)

        self.home_text = QLabel("Welcome,", self)
        self.home_text.setObjectName("home_text")
        self.home_text.setFixedSize(66, 16)
        self.home_text.move(30, 38)

        self.home_bold_text = QLabel("Professor Kinsley Samuel", self)
        self.home_bold_text.setObjectName("home_bold_text")
        self.home_bold_text.setFixedSize(192, 19)
        self.home_bold_text.move(30, 58)

        self.image_label = QLabel(self)
        self.image_label.setObjectName("image_label")
        pixmap = get_rounded_image()
        self.image_label.setPixmap(pixmap)
        self.image_label.setFixedSize(pixmap.size())
        self.image_label.move(250, 38)

        self.home_text2 = QLabel("What do you want to do today?", self)
        self.home_text2.setObjectName("home_text")
        self.home_text2.setFixedSize(159, 32)
        self.home_text2.move(33, 146)
        self.home_text2.setWordWrap(True)

        self.capture_button = QPushButton("Capture Student Data", self)
        self.capture_button.setObjectName("action")
        self.capture_button.setFixedSize(260, 50)
        self.capture_button.move(33, 196)
        self.capture_button.clicked.connect(self.eduttend.showDataCaptureScreen)

        self.take_button = QPushButton("Take Attendance", self)
        self.take_button.setObjectName("action")
        self.take_button.setFixedSize(260, 50)
        self.take_button.move(33, 284)
        self.take_button.clicked.connect(self.eduttend.showCourseSelectionScreen)
