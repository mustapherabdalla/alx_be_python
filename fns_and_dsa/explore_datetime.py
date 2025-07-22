from _datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    return current_date

print(f"Current date and time: {display_current_datetime().strftime("%Y-%m-%d %H:%M:%S")}")


number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    future_date = display_current_datetime() + timedelta(days=number_of_days)
    print(future_date.strftime("%Y-%m-%d"))

calculate_future_date()
