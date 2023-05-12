from PyQt5.QtWidgets import *
from view import *


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

cookie_count = 0
sandwich_count = 0
water_count = 0
cart_total = 0

class Controller(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.button_shop.clicked.connect(lambda: self.shop())
        self.button_exit.clicked.connect(lambda: self.exit())
        self.button_submit.clicked.connect(lambda: self.submit())

        self.label_grandtotal.setText('')
        self.label_notification.hide()
        self.main_menu()


    def main_menu(self):
        """
        Method to display the main menu format.
        """

        self.button_shop.show()
        self.button_exit.show()

        self.label_cartmenu.hide()
        self.label_mainmenu.show()

        self.button_submit.hide()

        self.label_cookie.hide()
        self.label_sandwich.hide()
        self.label_water.hide()
        self.input_cookie.hide()
        self.input_sandwich.hide()
        self.input_water.hide()


    def shop(self):
        """
        Method to display the shopping format when shop is clicked.
        """

        self.button_shop.hide()
        self.button_exit.hide()
        self.label_notification.setText("")


        self.label_cartmenu.show()
        self.label_mainmenu.hide()

        self.button_submit.show()

        self.label_cookie.show()
        self.label_sandwich.show()
        self.label_water.show()
        self.input_cookie.show()
        self.input_sandwich.show()
        self.input_water.show()



    def submit(self):
        """
        Method to add items when submit is clicked.
        """

        global cookie_count
        global sandwich_count
        global water_count
        global cart_total

        cookie_num = self.input_cookie.text()
        sandwich_num = self.input_sandwich.text()
        water_num = self.input_water.text()



        if cookie_num != '' or sandwich_num != '' or water_num != '':
            try:
                
                if cookie_num != '':
                    cookie_int = int(cookie_num)
                    cookie_count += cookie_int
                    new_total = cookie_int * 1.50
                    cart_total += new_total
                    
                    
                if sandwich_num != '':
                    sandwich_int = int(sandwich_num)
                    sandwich_count += sandwich_int
                    new_total = sandwich_int * 4.00
                    cart_total += new_total
                    

                if water_num != '':
                    water_int = int(water_num)
                    water_count += water_int
                    new_total = water_int * 1.00
                    cart_total += new_total
                    

                self.label_notification.setText("Added items")
                self.label_notification.show()
                self.main_menu()
                self.label_error.setText('')
                self.input_cookie.setText('')
                self.input_sandwich.setText('')
                self.input_water.setText('')
            
            except:
                self.label_error.setText("Please only enter whole numbers.")
                self.input_cookie.setText('')
                self.input_sandwich.setText('')
                self.input_water.setText('')

        else:
            self.label_error.setText("Please enter item amounts.")




    def exit(self):
        """
        Method to display the total when exit is clicked.
        """

        self.button_shop.hide()
        self.button_exit.hide()
        self.label_notification.setText("")

        self.label_cartmenu.hide()
        self.label_mainmenu.hide()

        self.button_submit.hide()

        self.label_cookie.hide()
        self.label_sandwich.hide()
        self.label_water.hide()
        self.input_cookie.hide()
        self.input_sandwich.hide()
        self.input_water.hide()


        self.label_grandtotal.setText(f'----------------------------------\n({cookie_count}) - Cookie = ${cookie_count * 1.5:.2f}\n({sandwich_count}) - Sandwich = ${sandwich_count * 4:.2f}\n({water_count}) - Water = ${water_count:.2f}\n----------------------------------\nGRAND TOTAL = ${cart_total:.2f}\n----------------------------------')
