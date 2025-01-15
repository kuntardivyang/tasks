# Use timedelta to:
# Schedule a recurring task every 5 minutes for the next hour.
from datetime import datetime, timedelta
current_time = datetime.now()
final_time = current_time + timedelta(hours=1)
schedule_time = timedelta(minutes=5)

while current_time <= final_time:
    print(f'Task Scheduled Now : {current_time.strftime('%d/%m/%Y %H:%M:%S')}')
    current_time += schedule_time

# Calculate the age of a person based on their birthdate.
birthday = input('Enter your birthdate in this format 11/03/2005  : ')
birthday = datetime.strptime(birthday, "%d/%m/%Y")
current_date = datetime.now()
Age = current_date.year - birthday.year
if (current_date.month, current_date.day) < (birthday.month, birthday.day): 
    Age -= 1
print('Your age is', Age)