

from PyQt5.QtWidgets import QApplication, QWidget
import sys


class MainWin():
    
    #初始化
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        ##追加一行注释
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWin()
    ui.show()
    sys.exit(app.exec_())