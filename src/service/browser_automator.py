# src/service/browser_automator_optimized.py

import logging
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from .locators import (
    FirstPageLocators, DatePickerLocators, SecondPageLocators,
    ConfirmationPopupLocators, ResultPageLocators
)


class BrowserAutomator:
    """
    Handles low-level browser interactions using Selenium.
    This class is now focused solely on browser actions, not the business workflow.
    """

    def __init__(self, url: str, headless: bool = True, logger=None):
        self.url = url
        self.headless = headless
        self.driver = None
        self.wait = None
        self.logger = logger or logging.getLogger(__name__)

    def setup_driver(self):
        """Sets up Chrome or Edge WebDriver."""
        self.logger.info("Setting up WebDriver...")
        try:
            self._setup_chrome()
        except Exception as chrome_error:
            self.logger.warning(f"Chrome WebDriver setup failed: {chrome_error}. Trying Edge.")
            try:
                self._setup_edge()
            except Exception as edge_error:
                self.logger.critical(f"Edge WebDriver setup failed: {edge_error}")
                raise RuntimeError("All WebDriver setups failed.") from edge_error

        self.wait = WebDriverWait(self.driver, 15)  # Increased timeout slightly for reliability
        self.logger.info(f"{self.driver.name.capitalize()} WebDriver initiated.")

    def _setup_chrome(self):
        """Configures and initializes the Chrome WebDriver."""
        options = ChromeOptions()
        if self.headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)

    def _setup_edge(self):
        """Configures and initializes the Edge WebDriver."""
        options = EdgeOptions()
        if self.headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        service = EdgeService(EdgeChromiumDriverManager().install())
        self.driver = webdriver.Edge(service=service, options=options)

    def open_site(self):
        """Navigates to the specified URL and waits for the page to load."""
        if not self.driver:
            raise RuntimeError("WebDriver is not initialized. Call setup_driver() first.")
        self.logger.info(f"Loading page: {self.url}")
        self.driver.get(self.url)
        if not self.headless:
            self.driver.maximize_window()
        self.wait_for_element(FirstPageLocators.METER_INPUT)
        self.logger.info("Payment page loaded successfully.")

    def close(self):
        """Closes the browser and cleans up resources."""
        if self.driver:
            self.logger.info("Closing browser.")
            self.driver.quit()
            self.driver = None
            self.wait = None

    # --- Generic Wrapper Methods ---
    def click_element(self, locator: tuple):
        """Finds a clickable element and clicks it."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys_to_element(self, locator: tuple, keys: str):
        """Finds an element, clears it, and sends keys."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(keys)

    def get_element_text(self, locator: tuple) -> str:
        """Finds an element and returns its text."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text.strip()

    def wait_for_element(self, locator: tuple, timeout: int = 10) -> WebElement:
        """Explicitly waits for an element to be visible."""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def find_optional_element_text(self, locator: tuple) -> str | None:
        """Tries to find an element and get its text without failing."""
        try:
            # Use a short timeout to avoid long waits for non-existent elements
            element = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locator))
            return element.text.strip()
        except TimeoutException:
            return None

    # --- Specific Date Picker Logic ---
    def select_expiry_date(self, month: int, year: int):
        """Handles the complex date picker interaction."""
        self.click_element(FirstPageLocators.EXPIRY_POPUP_BUTTON)
        self.wait_for_element(DatePickerLocators.JAN_LINK)  # Wait for picker to be visible

        # Select Year
        self._select_year_in_picker(year)

        # Select Month
        month_map = {
            1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
            7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
        }
        month_str = month_map.get(month)
        if not month_str:
            raise ValueError(f"Invalid month: {month}")

        month_locator = (By.XPATH, DatePickerLocators.MONTH_XPATH_TEMPLATE.format(month_str=month_str))
        self.click_element(month_locator)

        # Confirm selection
        self.click_element(DatePickerLocators.OK_BUTTON)

    def _select_year_in_picker(self, target_year: int):
        """Navigates the year view in the date picker."""
        while True:
            years = self.driver.find_elements(*DatePickerLocators.VISIBLE_YEARS_XPATH)
            visible_years = [int(y.text) for y in years if y.text.isdigit()]

            if not visible_years:
                raise RuntimeError("Could not find any years in the date picker.")

            if min(visible_years) <= target_year <= max(visible_years):
                year_locator = (By.XPATH, DatePickerLocators.YEAR_XPATH_TEMPLATE.format(year=target_year))
                self.click_element(year_locator)
                return  # Year found and clicked

            # Decide which direction to navigate
            nav_button = DatePickerLocators.NEXT_YEAR_BUTTON if target_year > max(
                visible_years) else DatePickerLocators.PREV_YEAR_BUTTON
            self.click_element(nav_button)
            # Add a small wait for the animation/update to complete
            self.wait.until(EC.staleness_of(years[0]))