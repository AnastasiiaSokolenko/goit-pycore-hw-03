from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Convert string to datetime.date object
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        # Replace year with current year
        birthday_this_year = birthday.replace(year=today.year)

        # If birthday already passed this year, take it from next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Check if the birthday is within the next 7 days (including today)
        delta_days = (birthday_this_year - today).days
        if 0 <= delta_days <= 7:
            # Adjust for weekend: move to Monday if birthday is on Sat or Sun
            if birthday_this_year.weekday() == 5:  # Saturday
                congratulation_date = birthday_this_year + timedelta(days=2)
            elif birthday_this_year.weekday() == 6:  # Sunday
                congratulation_date = birthday_this_year + timedelta(days=1)
            else:
                congratulation_date = birthday_this_year

            # Format the congratulation date as 'YYYY.MM.DD'
            congratulation_date_str = congratulation_date.strftime("%Y.%m.%d")
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })

    return upcoming_birthdays

# Example usage:
users = [
    {"name": "John Doe",  "birthday": "1985.01.23"},
    {"name": "Jane Smith","birthday": "1990.01.27"},
    {"name": "Dave Green",  "birthday": "1970.06.22"},
    {"name": "Alice Smith","birthday": "2000.06.20"},
]

print(get_upcoming_birthdays(users)) #[{'name': 'Dave Green', 'congratulation_date': '2025.06.23'}, {'name': 'Alice Smith', 'congratulation_date': '2025.06.20'}]