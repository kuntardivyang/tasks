# Write a program to:
# Display the current date and time in the format YYYY-MM-DD HH:MM:SS.
from datetime import datetime

today = datetime.now()
result = today.strftime("%Y-%m-%d %H:%M:%S")
print(f"current date and time: {result}")

# Parse a date string (e.g., "2025-01-01") into a datetime object.
d_string = input('Enter a date in this format "2025-01-01" : ').strip().split('-')
datetime_object = datetime(*map(int, d_string))
print(f'Datetime Object : {datetime_object}')