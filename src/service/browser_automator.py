from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class BrowserAutomator:
    """
    Class BrowserAutomator
    Controls browser to automate process of purchasing power OR water token using Selenium.
    """
    def __init__(self, url: str, headless: bool = False, skip_setup: bool = False):
        self.url = url
        self.headless = headless
        self.driver = None
        self.wait = None
        if not skip_setup:
            self._setup_driver()


    def _setup_driver(self):
        """
        Sets up Chrome WebDriver by default.
        Falls back to Microsoft Edge WebDriver if Chrome is not available
        """
        self.wait_timeout = 5
        chrome_options = ChromeOptions()
        edge_options = EdgeOptions()

        if self.headless:
            for opts in [chrome_options, edge_options]:
                opts.add_argument("--headless")
                opts.add_argument("--disable-gpu")
                opts.add_argument("--no-sandbox")
                opts.add_argument("--disable-dev-shm-usage")

        try:
            # setup Chrome WebDriver
            service = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.wait = WebDriverWait(self.driver, self.wait_timeout)
            # log.info("Chrome initiated")
        except Exception as chrome_error:
            chrome_msg = f"Chrome WebDriver failed: {chrome_error}"
            # log.warning(chrome_msg)
            try:
                # setup Microsoft Edge WebDriver if Chrome unavailable
                service = EdgeService(EdgeChromiumDriverManager().install())
                self.driver = webdriver.Edge(service=service, options=edge_options)
                self.wait = WebDriverWait(self.driver, self.wait_timeout)
                # log.info("Edge initiated")
            except Exception as edge_error:
                edge_msg = f"Edge WebDriver failed: {edge_error}"
                # log.critical(edge_msg)
                raise RuntimeError("WebDriver initiation failed") from edge_error