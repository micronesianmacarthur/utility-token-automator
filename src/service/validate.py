class Validate:
    def meterNo(self, value):
        """
        Validate Meter Number is not empty and is numeric.
        :param value: (str) Meter Number.
        :return: (bool)
        """
        if value:
            try:
                int(value)
                return True, "Valid Meter Number"
            except (TypeError, ValueError):
                return False, "Invalid Meter Number"
        return False, "Meter Number is required"

    def amount(self, value):
        """
        Validate Amount is not empty and is numeric.
        :param value: (str) Amount.
        :return: (bool), (float) Amount, (str) message
        """
        if value:
            try:
                value = float(value)
                if value < 5:
                    return False, value, "Amount cannot be less than 5"
                return True, value, "Valid Amount"
            except (TypeError, ValueError):
                return False, value, "Invalid Amount"
        return False, value, "Amount is required"

    def cc_details(self, name, number, code, month, year):
        if not all ([name, number, code, month, year]):
            return False, "Missing CC environment variables"
        return True, "CC environment variables set"

    @staticmethod
    def luhn_validation(cc_number):
        """Validates cc number using the Luhn algorithm."""
        if not cc_number.isdigit():
            raise Exception("Invalid CC Number")

        digits = [int(d) for d in cc_number]
        total = 0
        is_second_digit = False

        # iterate from rightmost digit
        for i in range(len(digits)):
            digit = digits[i]
            if is_second_digit:
                digit *= 2
                if digit > 9:
                    digit = digit % 10 + 1

            total += digit
            is_second_digit = not is_second_digit

        return total % 10 == 0
