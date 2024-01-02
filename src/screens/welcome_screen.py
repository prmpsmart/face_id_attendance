from ..shared.base_screen import *


class WelcomeScreen(BaseScreen):
    def __init__(self, *args):
        super().__init__(*args)

        self.image_label = QLabel(self)
        pixmap = QPixmap(":/logo").scaled(116, 135)
        self.image_label.setPixmap(pixmap)
        self.image_label.setFixedSize(pixmap.size())
        self.image_label.move(100, 70)

        self.welcome_text = QLabel("Welcome", self)
        self.welcome_text.setObjectName("welcome_text")
        self.welcome_text.setFixedSize(126, 40)
        self.welcome_text.move(97, 263)

        self.sign_in_button = QPushButton("Sign In", self)
        self.sign_in_button.setObjectName("action")
        self.sign_in_button.setFixedSize(260, 50)
        self.sign_in_button.move(30, 361)
        # self.sign_in_button.clicked.connect(self.eduttend.showSignInScreen)
        self.sign_in_button.clicked.connect(self.eduttend.showFaceIDLoginScreen)
