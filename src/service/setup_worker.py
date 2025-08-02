from PySide6.QtCore import QObject, Signal, Slot

from .browser_automator import BrowserAutomator


class SetupWorker(QObject):
    finished = Signal(object)
    error = Signal(str)

    def __init__(self, url, logger):
        super().__init__()
        self.url = url
        self.logger = logger

    def run(self):
        try:
            automator = BrowserAutomator(url=self.url, headless=True, logger=self.logger, skip_setup=True)
            automator.setup_driver()
            automator.open_site()
            self.finished.emit(automator)
        except Exception as e:
            self.error.emit(str(e))
