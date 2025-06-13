from datetime import datetime
def get_days_from_today(date: str) -> int:
    """
    Calculates the number of days between the given date and today's date.
    
    :param date: A string representing a date in the format 'YYYY-MM-DD'.
    :return: An integer representing the number of days from the given date to the current one. If the given date is in the future, the result will be negative.
    """
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        today_date = datetime.today().date()
        delta = today_date - input_date
        return delta.days
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

# Example of user interaction:
if __name__ == "__main__":
    while True:
        user_input = input("Enter a date in format YYYY-MM-DD: ")
        try:
            days_difference = get_days_from_today(user_input)
            print(f"Number of days from {user_input} to today: {days_difference}")
            break  # Exit loop if input is valid
        except ValueError as e:
            print(f"Error: {e} Please try again.\n")