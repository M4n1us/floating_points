from PyQt5.QtWidgets import QMessageBox

def openInfoPopup(window, title, text):
    return QMessageBox.information(window, title, text, QMessageBox.Ok)
