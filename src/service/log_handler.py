# src.service.log_handler

import logging
from PySide6.QtWidgets import QStatusBar

class LogHandler(logging.Handler):
    """
    A custom logging handler that displays log messages in a QStatusBar.
    """
    def __init__(self, status_bar: QStatusBar, default_timeout: int = 5000):
        """
        Args:
            status_bar: The QStatusBar widget to display messages on.
            default_timeout: The default time in milliseconds to show messages.
        """
        super().__init__()
        self.status_bar = status_bar
        self.default_timeout = default_timeout

    def emit(self, record: logging.LogRecord):
        """Formats and displays the log record."""
        msg = self.format(record)
        self.status_bar.showMessage(msg, self.default_timeout)