from ..shared.commons import *
from ..shared.base_screen import BaseScreen


class LaunchScreen(BaseScreen):
    def __init__(self, *args):
        super().__init__(*args)

        self.image_label = QLabel(self)
        pixmap = QPixmap(":/logo").scaled(160, 188)
        self.image_label.setPixmap(pixmap)
        self.image_label.setFixedSize(pixmap.size())
        self.image_label.move(80, 82)

        QTimer.singleShot(
            1000,
            self.eduttend.showWelcomeScreen,
        )
