# Write a program to:
# Calculate the number of weekends between two given dates.
# Display the weekday name for a user-provided date.
from datetime import datetime, timedelta

first_date = datetime.strptime(input("Enter the first date in this format (DD/MM/YYYY): "), "%d/%m/%Y")
second_date = datetime.strptime(input("Enter the end date in this format (DD/MM/YYYY): "), "%d/%m/%Y")

weekends = []
current_date = first_date

while current_date <= second_date:
    if current_date.weekday() == 5 or current_date.weekday() == 6:
        weekends.append(current_date)
    current_date += timedelta(days=1)

print(f"The number of weekends between {first_date} and {second_date} is {len(weekends)}")
date = datetime.strptime(input("Enter a date in this format (DD/MM/YYYY): "), "%d/%m/%Y")
print('Weekday name of provided date is ', date.strftime('%A'))