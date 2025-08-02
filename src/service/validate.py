# src/service/validate_optimized.py

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


class Validate:
    """
    Provides static methods for input validation.
    Methods raise ValidationError on failure for clear, Pythonic error handling.
    """

    @staticmethod
    def meter_num(value: str):
        """
        Validates that the Meter Number is a non-empty string of digits.

        Raises:
            ValidationError: If validation fails.
        """
        if not value or not value.strip():
            raise ValidationError("Meter Number is required.")
        if not value.isdigit():
            raise ValidationError("Invalid Meter Number: must contain only digits.")

    @staticmethod
    def amount(value: str):
        """
        Validates the purchase amount.

        Returns:
            float: The validated and converted amount.

        Raises:
            ValidationError: If validation fails.
        """
        if not value or not value.strip():
            raise ValidationError("Amount is required.")
        try:
            amount_val = float(value)
            if amount_val < 5.0:
                raise ValidationError("Amount cannot be less than $5.00.")
            return amount_val
        except (ValueError, TypeError):
            raise ValidationError("Invalid Amount: must be a number.")