from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QWidget
from . import resource


class MainWindow:
    def showWelcomeScreen(self):
        raise NotImplementedError

    def showSignInScreen(self):
        raise NotImplementedError

    def showFingerprintLoginScreen(self):
        raise NotImplementedError

    def showFaceIDLoginScreen(self):
        raise NotImplementedError

    def showApprovedScreen(self):
        raise NotImplementedError

    def showDenyScreen(self):
        raise NotImplementedError

    def showHomeScreen(self):
        raise NotImplementedError

    def showCourseSelectionScreen(self):
        raise NotImplementedError

    def showTimerScreen(self):
        raise NotImplementedError

    def showChooseAttendanceScreen(self):
        raise NotImplementedError

    def showFingerprintFeedbackScreen(self):
        raise NotImplementedError

    def showFaceIDFeedbackScreen(self):
        raise NotImplementedError

    def showDataCaptureScreen(self):
        raise NotImplementedError

    def showFaceIDCaptureScreen(self):
        raise NotImplementedError

    def showFingerprinCaptureScreen(self):
        raise NotImplementedError


class Notify(QFrame):
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

    def show_accepted(self):
        self.update_notify(error=False)

    def show_captured(self):
        self.update_notify(error=False)

    def show_rejected(self):
        self.update_notify()

    def show_not_registered(self):
        self.update_notify(not_found=True)

    def update_notify(
        self,
        captured: bool = False,
        error: bool = True,
        not_found: bool = False,
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

        QTimer.singleShot(500, self.hide)


def get_rounded_image() -> QPixmap:
    pixmap = QPixmap(":/student").scaled(40, 40)

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
