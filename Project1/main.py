from controller import *

def main():

    app = QApplication([])
    window = Controller()
    window.setWindowTitle('Project 1')
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()