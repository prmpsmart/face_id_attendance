from .shared.commons import *
from .screens.launch_screen import LaunchScreen
from .screens.welcome_screen import WelcomeScreen
from .screens.sign_in_screen import SignInScreen
from .screens.fingerprint_login_screen import FingerprintLoginScreen
from .screens.face_id_login_screen import FaceIDLoginScreen
from .screens.approved_screen import ApprovedScreen
from .screens.deny_screen import DenyScreen
from .screens.home_screen import HomeScreen
from .screens.course_selection_screen import CourseSelectionScreen
from .screens.timer_screen import TimerScreen
from .screens.choose_attendance_screen import ChooseAttendanceScreen
from .screens.fingerprint_feedback_screen import FingerprintFeedbackScreen
from .screens.face_id_feedback_screen import FaceIDFeedbackScreen
from .screens.data_capture_screen import DataCaptureScreen
from .screens.face_id_capture_screen import FaceIDCaptureScreen
from .screens.fingerprint_capture_screen import FingerprinCaptureScreen


class Eduttend(QMainWindow, MainWindow):
    def __init__(self, title: str) -> None:
        QMainWindow.__init__(self)

        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(":/logo"))

        # self.setCentralWidget(LaunchScreen(self))
        self.showFaceIDCaptureScreen()

    def mousePressEvent(self, a0) -> None:
        QApplication.instance().quit()

    def showWelcomeScreen(self):
        self.setCentralWidget(WelcomeScreen(self))

    def showSignInScreen(self):
        self.setCentralWidget(SignInScreen(self))

    def showFingerprintLoginScreen(self):
        self.setCentralWidget(FingerprintLoginScreen(self))

    def showFaceIDLoginScreen(self):
        self.setCentralWidget(FaceIDLoginScreen(self))

    def showApprovedScreen(self):
        self.setCentralWidget(ApprovedScreen(self))

    def showDenyScreen(self):
        self.setCentralWidget(DenyScreen(self))

    def showHomeScreen(self):
        self.setCentralWidget(HomeScreen(self))

    def showCourseSelectionScreen(self):
        self.setCentralWidget(CourseSelectionScreen(self))

    def showTimerScreen(self):
        self.setCentralWidget(TimerScreen(self))

    def showChooseAttendanceScreen(self):
        self.setCentralWidget(ChooseAttendanceScreen(self))

    def showFingerprintFeedbackScreen(self):
        self.setCentralWidget(FingerprintFeedbackScreen(self))

    def showFaceIDFeedbackScreen(self):
        self.setCentralWidget(FaceIDFeedbackScreen(self))

    def showDataCaptureScreen(self):
        self.setCentralWidget(DataCaptureScreen(self))

    def showFaceIDCaptureScreen(self):
        self.setCentralWidget(FaceIDCaptureScreen(self))

    def showFingerprinCaptureScreen(self):
        self.setCentralWidget(FingerprinCaptureScreen(self))

