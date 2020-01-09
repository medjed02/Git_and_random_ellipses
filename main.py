import sys
from Window import Ellipses
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ellipses()
    ex.show()
    sys.exit(app.exec_())