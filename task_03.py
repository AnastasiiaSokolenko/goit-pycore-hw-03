import re

def normalize_phone(phone_number: str) -> str:
    """
    Normalizes a phone number to the standard format:
    - Removes all characters except digits and '+'.
    - Ensures the number starts with '+', adding '+38' (Ukraine code) if needed.

    :param phone_number: A string containing a phone number in any format.
    :return: Normalized phone number as a string.
    """
    # Remove all characters except digits and '+'
    cleaned = re.sub(r'[^\d+]', '', phone_number.strip())

    # If the number already starts with '+', assume it's properly international
    if cleaned.startswith('+'):
        return cleaned

    # If the number starts with '380', just add '+'
    if cleaned.startswith('380'):
        return '+' + cleaned

    # If the number starts with anything else (like '050', '067'), add '+38'
    return '+38' + cleaned


# Example usage:
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
