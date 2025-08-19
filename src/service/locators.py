# src.service.locators

from selenium.webdriver.common.by import By


class FirstPageLocators:
    """Locators for first page."""
    METER_INPUT = (By.ID, "ctl00_ContentPlaceHolder1_radTxtMeter")
    CC_NUMBER_INPUT = (By.ID, "ctl00_ContentPlaceHolder1_rtxtCreditCardNumber")
    CC_NAME_INPUT = (By.ID, "ctl00_ContentPlaceHolder1_txtCardholderName")
    CC_CODE_INPUT = (By.ID, "ctl00_ContentPlaceHolder1_txtCardCode")
    EXPIRY_POPUP_BUTTON = (By.ID, "ctl00_ContentPlaceHolder1_dtpExpirationDate_popupButton")
    NEXT_BUTTON = (By.ID, "ctl00_ContentPlaceHolder1_btnNext_input")
    METER_ERROR_LABEL = (By.ID, "ContentPlaceHolder1_lblmeter")

class DatePickerLocators:
    """Locators for the date picker calendar popup."""
    JAN_LINK = (By.ID, "rcMView_Jan")  # Used to wait for the picker to be visible
    MONTH_XPATH_TEMPLATE = "//td[@id='{month_str}']//a"
    YEAR_XPATH_TEMPLATE = "//td[@id='rcMView_{year}']//a"
    NEXT_YEAR_BUTTON = (By.ID, "ctl00_ContentPlaceHolder1_dtpExpirationDate_dtpExpirationDate_NavigationNextLink")
    PREV_YEAR_BUTTON = (By.ID, "ctl00_ContentPlaceHolder1_dtpExpirationDate_dtpExpirationDate_NavigationPrevLink")
    VISIBLE_YEARS_XPATH = "//td[starts-with(@id, 'rcMView_') and string-length(substring-after(@id, 'rcMView_')) = 4 and number(substring-after(@id, 'rcMView_')) = substring-after(@id, 'rcMView_')]//a"
    OK_BUTTON = (By.ID, "rcMView_OK")

class SecondPageLocators:
    """Locators for the second page."""
    CUSTOMER_NAME_FIRST = (By.ID, "ctl00_ContentPlaceHolder1_radLblConsumerFirstName")
    CUSTOMER_NAME_LAST = (By.ID, "ctl00_ContentPlaceHolder1_radLblConsumerSurname")
    OTHER_AMOUNT_RADIO = (By.ID, "ctl00_ContentPlaceHolder1_radlAmount_ctl04")
    AMOUNT_INPUT = (By.ID, "ctl00_ContentPlaceHolder1_radNumericTxtAmount")
    NEXT_BUTTON = (By.ID, "ctl00_ContentPlaceHolder1_btnNext_input")

class ConfirmationPopupLocators:
    """Locators for the final payment confirmation popup."""
    SUBMIT_BUTTON = (By.ID, "ctl00_ContentPlaceHolder1_RadWindow1_C_rbtnSave_input")

class ResultPageLocators:
    """Locators for the final page showing the token or error."""
    TOKEN_LABEL = (By.ID, "ctl00_ContentPlaceHolder1_radLblVouchers")
    ERROR_TITLE = (By.ID, "LeftTitle")
    ERROR_DETAIL_XPATH = "//div[@style='font-size: 14px; text-align: left; word-break: break-all;']"