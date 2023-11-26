from .commons import *


class BaseScreen(QWidget):
    def __init__(self, eduttend: MainWindow):
        super().__init__()

        self.eduttend = eduttend
