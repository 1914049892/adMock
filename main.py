# -*- encoding=utf8 -*-

import sys

from PyQt5 import QtWidgets

from DWindows import TabWidget

if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  mainWindow = TabWidget()
  mainWindow.show()
  sys.exit(app.exec_())
