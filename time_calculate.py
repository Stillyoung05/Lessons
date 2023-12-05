from datetime import datetime


def time_passed_from_given_date(given_date):
    given_datetime = datetime.strptime(given_date, '%Y-%m-%d')
    current_datetime = datetime.now()
    time_difference = current_datetime - given_datetime
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"


given_date_str = input("Enter the time you need, \nin the following {2023-01-0} format: ")
time_passed = time_passed_from_given_date(given_date_str)
print(f"Time passed since {given_date_str}: {time_passed}")
