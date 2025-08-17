# src.service.log_handler

import logging
from PySide6.QtWidgets import QStatusBar


DEFAULT_TIMEOUT = 5000

class LogHandler(logging.Handler):
    """A custom logging handler that displays messages in QStatusBar"""
    def __init__(self, status_bar: QStatusBar, default_timeout: int = DEFAULT_TIMEOUT):
        super().__init__()
        self.status_bar = status_bar
        self.default_timeout = default_timeout

    def emit(self, record: logging.LogRecord):
        msg = self.format(record)
        self.status_bar.showMessage(msg, self.default_timeout)
