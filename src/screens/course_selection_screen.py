from ..shared.base_screen import *


class CourseSelectionScreen(BaseScreen):
    def __init__(self, *args, profile: Profile):
        super().__init__(*args)

        self.course_selection_text = QLabel("Course", self)
        self.course_selection_text.setObjectName("bold_text")
        self.course_selection_text.setFixedSize(56, 16)
        self.course_selection_text.move(30, 35)

        self.course_selection_text = QLabel("Selection", self)
        self.course_selection_text.setObjectName("bold_text")
        self.course_selection_text.setFixedSize(77, 19)
        self.course_selection_text.move(30, 55)

        self.image_label = QLabel(self)
        self.image_label.setObjectName("image_label")
        pixmap = get_rounded_image(profile.image)
        self.image_label.setPixmap(pixmap)
        self.image_label.setFixedSize(pixmap.size())
        self.image_label.move(250, 35)

        self.select_combobox = QComboBox(self)
        self.select_combobox.setFixedSize(260, 50)
        self.select_combobox.move(31, 169)

        self.select_combobox.addItems(
            [
                "EEE 501",
                "EEE 502",
                "EEE 503",
                "EEE 504",
                "EEE 505",
                "EEE 506",
            ]
        )

        self.select_button = QPushButton("Select Course", self)
        self.select_button.setObjectName("action")
        self.select_button.setFixedSize(260, 50)
        self.select_button.move(31, 260)
        self.select_button.clicked.connect(self.eduttend.showTimerScreen)
