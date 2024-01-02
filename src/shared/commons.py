from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtGui import QHideEvent, QMouseEvent
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QWidget
from . import resource


class Notify(QFrame):
    hidden = Signal()

    def __init__(self, parent: QWidget):
        super().__init__(parent)

        lay = QVBoxLayout(self)

        self.icon = QLabel()
        lay.addWidget(self.icon, 0, Qt.AlignmentFlag.AlignCenter)

        self.text = QLabel()
        lay.addWidget(self.text, 0, Qt.AlignmentFlag.AlignCenter)
        self.text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        effect = QGraphicsDropShadowEffect()
        effect.setOffset(1, 1)
        self.setGraphicsEffect(effect)

        self.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
        self.setLineWidth(1)

        self.hide()

    def setEffect(self, color: str):
        effect = QGraphicsDropShadowEffect()
        effect.setOffset(1, 1)
        effect.setColor(QColor(color))
        self.setGraphicsEffect(effect)

    def show_accepted(self, interval: int = 0):
        self.update_notify(error=False, interval=interval)

    def show_captured(self, interval: int = 0):
        self.update_notify(error=False, interval=interval)

    def show_rejected(self, interval: int = 0):
        self.update_notify(interval=interval)

    def show_not_registered(self, interval: int = 0):
        self.update_notify(not_found=True, interval=interval)

    def update_notify(
        self,
        captured: bool = False,
        error: bool = True,
        not_found: bool = False,
        interval: int = 0,
    ):
        if error:
            icon = "cancel_n"
            color = "#F50000"
            if not_found:
                text = "Student not Registered"
            else:
                text = "Try again!!!"
        else:
            color = "#05C847"
            icon = "check_n"
            if captured:
                text = "Captured Successfully"
            else:
                text = "Attendance taken"

        self.text.setText(text)
        self.icon.setPixmap(QPixmap(f":/{icon}"))
        self.setEffect(color)

        self.setStyleSheet(
            f"""
                Notify {{
                    border-bottom: 2px solid {color};
                    border-radius: 10px; 
                }}
                QLabel {{
                    color: {color};
                    font-family: Raleway;
                    font-size: 16px;
                    font-weight: 400;
                    line-height: 19px;
                    letter-spacing: 0em;
                    text-align: left;
                }}
            """
        )

        self.show()

        if interval:
            QTimer.singleShot(interval, self.hide)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.hide()
        return super().mousePressEvent(event)

    def hideEvent(self, event: QHideEvent) -> None:
        self.hidden.emit()
        return super().hideEvent(event)


def get_rounded_image(image=None) -> QPixmap:
    pixmap = QPixmap(image or ":/student").scaled(40, 40)

    target_pixmap = QPixmap(pixmap.size())
    target_pixmap.fill(Qt.transparent)

    painter = QPainter(target_pixmap)
    painter.setRenderHint(QPainter.Antialiasing, True)
    # painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
    painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

    path = QPainterPath()
    path.addRoundedRect(
        0,
        0,
        pixmap.width(),
        pixmap.height(),
        pixmap.width() / 2,
        pixmap.width() / 2,
    )

    painter.setClipPath(path)
    painter.drawPixmap(0, 0, pixmap)
    painter.end()

    return target_pixmap


class Profile:
    def __init__(self, image: QImage):
        self.image = image
        self.time: int = 0
