class Validate:
    @staticmethod
    def meter_num(value):
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

    @staticmethod
    def amount(value):
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

    @staticmethod
    def cc_details(name, number, code, month, year):
        if not all ([name, number, code, month, year]):
            return False, "Missing CC environment variables"
        return True, "CC environment variables set"