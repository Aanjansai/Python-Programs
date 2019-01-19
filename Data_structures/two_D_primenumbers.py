""" Take a range of 0 - 1000 Numbers and find the Prime numbers in that range. Store the prime numbers in a 2D Array,
    the first dimension represents the range 0-100, 100-200, and so on. While the second dimension represents
    the prime numbers in that range.
"""

from UtilityMethods.ds_utility import FunctionsOfOperations


def two_d_prime():
    """
        This method is act as runner for prime_number_2d_array() method.
    """
    logic_object = FunctionsOfOperations()

    print("List all prime numbers\n")

    logic_object.prime_number_2d_array()


if __name__ == "__main__":

    two_d_prime()
