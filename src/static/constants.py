# src/static/constants_optimized.py

import os

# The URL for the payment portal. Keeping it as a global constant is fine.
URL = "https://puc.able-soft.com:10131/ADR/PaymentADR_Step1.aspx"


class ConfigError(Exception):
    """Custom exception for configuration errors."""
    pass


def get_cc_details():
    """
    Retrieves credit card details from environment variables just-in-time.

    This is more secure than loading them as global variables at module import,
    as it reduces the time sensitive data is held in memory.

    Returns:
        dict: A dictionary containing the credit card details.

    Raises:
        ConfigError: If any of the required environment variables are missing.
    """
    required_vars = [
        "CC_NAME", "CC_NUMBER", "CC_CODE", "CC_EXP_MONTH", "CC_EXP_YEAR"
    ]

    cc_details = {var: os.getenv(var) for var in required_vars}

    missing_vars = [key for key, value in cc_details.items() if value is None]
    if missing_vars:
        raise ConfigError(f"Missing CC environment variables: {', '.join(missing_vars)}")

    # Basic type validation for month and year
    try:
        cc_details["CC_EXP_MONTH"] = int(cc_details["CC_EXP_MONTH"])
        cc_details["CC_EXP_YEAR"] = int(cc_details["CC_EXP_YEAR"])
    except (ValueError, TypeError):
        raise ConfigError("CC_EXP_MONTH and CC_EXP_YEAR must be valid integers.")

    return cc_details