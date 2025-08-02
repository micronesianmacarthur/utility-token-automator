import logging

from PySide6.QtWidgets import QMessageBox


class LogHandler(logging.Handler):
    def __init__(self, status_bar):
        super().__init__()
        self.status_bar = status_bar

    def emit(self, record):
        msg = self.format(record)
        self.status_bar.showMessage(msg) # add (msg, 5000) to show message for 5 seconds