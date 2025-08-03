# src/service/setup_worker_optimized.py

from PySide6.QtCore import QObject, Signal
from .browser_automator_optimized import BrowserAutomator

class SetupWorker(QObject):
    """
    QObject worker to set up the BrowserAutomator in a background thread.
    This prevents the UI from freezing during the potentially slow driver setup.
    """
    finished = Signal(BrowserAutomator)
    error = Signal(str)

    def __init__(self, url: str, logger):
        super().__init__()
        self.url = url
        self.logger = logger
        self.automator = None

    def run(self):
        """The task to be executed in the background thread."""
        try:
            self.automator = BrowserAutomator(url=self.url, headless=True, logger=self.logger)
            self.automator.setup_driver()
            self.automator.open_site()
            self.finished.emit(self.automator)
        except Exception as e:
            self.logger.critical(f"Setup worker failed: {e}", exc_info=True)
            # Ensure browser is closed on failure
            if self.automator:
                self.automator.close()
            self.error.emit(f"Failed to start browser: {e}")