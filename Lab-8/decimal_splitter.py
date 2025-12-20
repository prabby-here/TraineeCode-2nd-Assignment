class DecimalSplitter:
    """
    Method to get the whole number from a double
    """
    @staticmethod
    def get_whole(number):
        return int(number)

    """
    Method to get the fractional part of a double number
    """
    @staticmethod
    def get_fraction(number):
        whole = int(number)
        frac = number - whole
        return round(abs(frac), 10)

    """
    Method to check if a given number is odd or even
    """
    def is_odd(number):
        pass
