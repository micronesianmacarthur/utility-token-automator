# src.service.constants

import os


# Payment portal URL as global constant
URL = "https://puc.able-soft.com:10131/ADR/PaymentADR_Step1.aspx"

class ConfigError(Exception):
    """
    Custom exception for configuration errors
    """
    pass

def get_cc_details():
    """
    Retrieves CC details from environment variables in-time

    :return:
        dict: Dictionary containing the CC details

    :raises:
        ConfigError: If any of environment variables are missing.
    """
    required_vars = [
        "CC_NAME", "CC_NUMBER", "CC_CODE", "CC_EXP_MONTH", "CC_EXP_YEAR"
    ]

    cc_details = {var : os.getenv(var) for var in required_vars}

    missing_vars = [
        key for key, value in cc_details.items() if value is None
    ]

    if missing_vars:
        raise ConfigError(f"Missing CC environment variable: {', '.join(missing_vars)}")

    # basic type validation for month and year
    try:
        cc_details['CC_EXP_MONTH'] = int(cc_details['CC_EXP_MONTH'])
        cc_details['CC_EXP_YEAR'] = int(cc_details['CC_EXP_YEAR'])
    except (ValueError, TypeError):
        raise ConfigError(f"Expiry Month and Year must be valid integers")

    return cc_details