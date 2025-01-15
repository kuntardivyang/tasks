# Create a program that:
# Accepts two dates from the user and calculates the number of days between them.
# Adds 7 days to the current date and displays the result.
from datetime import datetime, timedelta

d_string = input('Enter first date in this format "2025-01-01" : ')
date1 = datetime.strptime(d_string, "%Y-%m-%d")
d_string = input('Enter first date in this format "2025-01-01" : ')
date2 = datetime.strptime(d_string, "%Y-%m-%d")

print('The Number of days between given dattes is : ', abs((date2 - date1).days))

current_date = datetime.now()
added_date = current_date + timedelta(days = 7)
print('current date after adding 7 days is : ', added_date)