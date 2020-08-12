import sys
from PyQt5 import QtCore, QtNetwork, QtWidgets

class CheckConnectivity(QtCore.QObject):
    sig = QtCore.pyqtSignal()
    def __init__(self, *args, **kwargs):
        QtCore.QObject.__init__(self, *args, **kwargs)
        url = QtCore.QUrl("https://www.google.com/")
        req = QtNetwork.QNetworkRequest(url)
        self.net_manager = QtNetwork.QNetworkAccessManager()
        self.res = self.net_manager.get(req)
        self.res.finished.connect(self.processRes)
        self.res.error.connect(self.processErr)
        self.msg = QtWidgets.QMessageBox()
        self.sig.
    @QtCore.pyqtSlot()
    def processRes(self):
        if self.res.bytesAvailable():
            self.msg.information(None, "Info", "You are connected to the Internet.")
        self.res.deleteLater()

    @QtCore.pyqtSlot(QtNetwork.QNetworkReply.NetworkError)
    def processErr(self, code):
        self.msg.critical(None, "Info", "You are not connected to the Internet.")
        print(code)
# class CheckConnectivity:
#     def __init__(self):
#         url = QtCore.QUrl("https://www.google.com/")
#         req = QtNetwork.QNetworkRequest(url)
#         net_manager = QtNetwork.QNetworkAccessManager()
#         self.res = net_manager.get(req)
#         self.res.finished.connect(self.processRes)
#         self.res.error.connect(self.processErr)
#         self.msg = QtWidgets.QMessageBox()
#
#     def processRes(self):
#         if self.res.bytesAvailable():
#             self.msg.information(self, "Info", "You are connected to the Internet.")
#         else:
#             self.msg.critical(self, "Info", "You are not connected to the Internet.")
#         self.msg.show()
#         self.res.close()
#
#     def processErr(self, *args):
#         print(*args)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ic = CheckConnectivity()
    sys.exit(app.exec_())