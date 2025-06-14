import random

def get_numbers_ticket(min, max, quantity) -> list:
    """
    Generates a sorted list of unique random numbers within a specified range.

    :param min: The minimum value of the range (inclusive) >= 1.
    :param max: The maximum value of the range (inclusive) <= 1000.
    :param quantity: The number of unique random numbers to generate.
    :return: A sorted list containing the generated unique random numbers. 
             If the parameters do not meet the specified constraints, the function returns an empty list.
    """

    if (not isinstance(min, int) or 
        not isinstance(max, int) or 
        not isinstance(quantity, int) or 
        min < 1 or 
        max > 1000 or 
        min >= max or 
        quantity < 1 or 
        quantity > (max - min + 1)):

        return []

    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)

# Example usage:
if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(0, 49, 6)
    print("Your lottery numbers:", lottery_numbers)