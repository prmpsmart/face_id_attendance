from .commons import *


try:
    from ..eduttend import Eduttend
except:
    ...


class BaseScreen(QWidget):
    def __init__(self, eduttend: "Eduttend"):
        super().__init__()

        self.eduttend = eduttend

    def make_request(self, interval: int = 1000):
        QTimer.singleShot(interval, self.on_request_timeout)

    def on_request_timeout(self):
        ...
