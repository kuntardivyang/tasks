# Write a program to:
# Generate a list of dates for the next 7 days.
from datetime import datetime, timedelta
current_date = datetime.now()
dates_list = [(current_date + timedelta(days=i)).strftime("%d-%m-%Y") for i in range(1, 8)]
for i, date in enumerate(dates_list):
    print(f'Date {i + 1} : {date}')
    
# Find all Mondays in the current month.
first_date = current_date.replace(day=1)
monday_list = []
current_date = first_date
while current_date.month == first_date.month:
    if current_date.weekday() == 0:
        monday_list.append(current_date.strftime("%d/%m/%Y"))
    current_date += timedelta(days=1)
print('Mondays List : ', monday_list)