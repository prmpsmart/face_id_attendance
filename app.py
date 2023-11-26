from src import *


class EduttendApp(QApplication):
    def __init__(
        self,
        argv: list[str] = [],
        title="Eduttend",
        width: int = 320,
        height: int = 480,
    ) -> None:
        super().__init__(argv)

        self.setStyleSheet(
            """
                WelcomeScreen QLabel#welcome_text {
                    font-family: Source Sans Pro;
                    font-size: 30px;
                    font-weight: 400;
                    line-height: 40px;
                    letter-spacing: 0em;
                    text-align: left;
                    color: #053DC8;
                }
                QPushButton#action {
                    font-family: Raleway;
                    font-size: 24px;
                    font-weight: 400;
                    line-height: 28px;
                    letter-spacing: 0em;
                    color: #FBFDFE;
                    background: #053DC8;
                    border-radius: 10px
                }
                QPushButton#action:hover {
                    background: #0435a6;
                }
                QPushButton#action:pressed {
                    background: #032471;
                }



                SignInScreen QLabel#signin_text {
                    font-family: Raleway;
                    font-size: 19px;
                    font-weight: 400;
                    line-height: 23px;
                    letter-spacing: 0em;
                    text-align: left;
                    color: #053DC8;
                }
                QPushButton#choose {
                    font-family: Raleway;
                    font-size: 24px;
                    font-weight: 400;
                    line-height: 28px;
                    letter-spacing: 0em;
                    color: black;
                    background: #FBFDFE;
                    border-radius: 10px
                }
                QPushButton#choose:hover {
                    background: #b8b9ba;
                }
                QPushButton#choose:pressed {
                    background: #8a8b8c;
                }



                FingerprintLoginScreen QLabel#fingerprint_login_text {
                    font-family: Raleway;
                    font-size: 20px;
                    font-weight: 400;
                    line-height: 23px;
                    letter-spacing: 0em;
                    color: #0021F5;
                }



                FaceIDLoginScreen QLabel#face_id_login_text {
                    font-family: Raleway;
                    font-size: 20px;
                    font-weight: 400;
                    line-height: 28px;
                    letter-spacing: 0em;
                    color: #0021F5;
                }



                ApprovedScreen QLabel#approved_text {
                    font-family: Raleway;
                    font-size: 23px;
                    font-weight: 400;
                    line-height: 28px;
                    letter-spacing: 0em;
                    color: #0021F5;
                }



                DenyScreen QLabel#deny_text_red {
                    font-family: Raleway;
                    font-size: 23px;
                    font-weight: 600;
                    line-height: 28px;
                    letter-spacing: 0em;
                    color: #F50000;
                }
                DenyScreen QLabel#deny_text {
                    font-family: Raleway;
                    font-size: 12px;
                    font-weight: 400;
                    line-height: 14px;
                    letter-spacing: 0em;
                    color: #0021F5;
                }



                HomeScreen QLabel#home_text {
                    font-family: Source Sans Pro;
                    font-size: 14px;
                    font-weight: 400;
                    line-height: 14px;
                    letter-spacing: 0em;
                    text-align: left;
                }
                HomeScreen QLabel#home_bold_text {
                    font-family: Raleway;
                    font-size: 15px;
                    font-weight: 600;
                    line-height: 16px;
                    letter-spacing: 0em;
                }
                HomeScreen QLabel#image_label {
                    border-radius: 20px;
                }



                QLabel#bold_text {
                    font-family: Raleway;
                    font-size: 16px;
                    font-weight: 600;
                    line-height: 19px;
                    letter-spacing: 0em;
                    text-align: left;
                }
                QComboBox {
                    color: black;
                    font: 14px;
                    padding: 1px 0px 1px 10px; 
                    border-radius: 10px;
                    border: 1px solid #0021F5;
                }
                
                QComboBox::drop-down 
                {
                    border: 1px;
                }

                /* Define a new custom arrow icon for the combo box */
                QComboBox::down-arrow {
                    image: url(:/arrow-down);
                    width: 14px;
                    height: 14px;
                    margin-right: 20px;
                }



                ChooseAttendanceScreen QLabel#take_text {
                    font-family: Raleway;
                    font-size: 20px;
                    font-weight: 400;
                    line-height: 23px;
                    letter-spacing: 0em;
                    text-align: center;
                    color: #053DC8;
                }



                QLabel#ff_text {
                    font-family: Raleway;
                    font-size: 13px;
                    font-weight: 400;
                    line-height: 15px;
                    letter-spacing: 0em;
                    text-align: left;
                }
                QLabel#ff_text3 {
                    font-family: Raleway;
                    font-size: 20px;
                    font-weight: 400;
                    line-height: 23px;
                    letter-spacing: 0em;
                    text-align: left;
                    color: #053DC8;
                }
                QLabel#ff_text4 {
                    font-family: Raleway;
                    font-size: 16px;
                    font-weight: 400;
                    line-height: 19px;
                    letter-spacing: 0em;
                    text-align: left;
                }



                QLabel#data_text {
                    font-family: Raleway;
                    font-size: 16px;
                    font-weight: 600;
                    line-height: 19px;
                    letter-spacing: 0em;
                    text-align: left;
                }
                QLineEdit {
                    border-radius: 10px;
                    border-bottom: 2px solid #053DC8;
                    padding: 10px;
                    font-size: 18px;
                }


            """
        )

        self.win = Eduttend(title)
        # self.win = QColorDialog()

        self.win.setFixedSize(width, height)
        # self.win.move(300, 100)
        self.win.move(1299, 36)
        self.win.show()


ea = EduttendApp()
ea.exec()
