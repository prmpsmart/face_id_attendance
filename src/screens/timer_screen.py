from ..shared.base_screen import *


class TimerScreen(BaseScreen):
    def __init__(self, *args):
        super().__init__(*args)

        self.timer_text = QLabel("Set", self)
        self.timer_text.setObjectName("bold_text")
        self.timer_text.setFixedSize(26, 20)
        self.timer_text.move(30, 35)

        self.timer_text = QLabel("Timer", self)
        self.timer_text.setObjectName("bold_text")
        self.timer_text.setFixedSize(48, 19)
        self.timer_text.move(30, 55)

        self.image_label = QLabel(self)
        self.image_label.setObjectName("image_label")
        pixmap = get_rounded_image()
        self.image_label.setPixmap(pixmap)
        self.image_label.setFixedSize(pixmap.size())
        self.image_label.move(250, 35)

        self.select_combobox = QComboBox(self)
        self.select_combobox.setFixedSize(260, 50)
        self.select_combobox.move(31, 169)

        self.select_combobox.addItems(
            [
                "15 mins",
                "30 mins",
                "45 mins",
                "No Timer",
            ]
        )

        self.set_timer_button = QPushButton("Set Timer", self)
        self.set_timer_button.setObjectName("action")
        self.set_timer_button.setFixedSize(260, 50)
        self.set_timer_button.move(30, 322)
        self.set_timer_button.clicked.connect(self.eduttend.showChooseAttendanceScreen)
