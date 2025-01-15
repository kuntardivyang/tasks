# Use the csv module to:
# Create a CSV file with student names and scores.
# Read the CSV file and calculate the average score.
import csv

fields = ['Name', 'Python Score', 'FSD Score', 'DM Score']

def create_csv(file_path):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)
        while True:
            name = input("Enter Student's Name: ")
            python_score = float(input("Enter Python Score: "))
            fsd_score = float(input("Enter FSD Score: "))
            dm_score = float(input("Enter DM Score: "))
            writer.writerow([name, python_score, fsd_score, dm_score])
            user_input = input("Do you want to stop? If yes, type 'QUIT' or press Enter to continue: ")
            if user_input.lower() == 'quit':
                break

def calculate_average(file_path):
    total_students = 0
    total_python_score = 0
    total_fsd_score = 0
    total_dm_score = 0
    
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            total_students += 1
            total_python_score += float(row['Python Score'])
            total_fsd_score += float(row['FSD Score'])
            total_dm_score += float(row['DM Score'])
    
    avg_python_score = total_python_score / total_students if total_students else 0
    avg_fsd_score = total_fsd_score / total_students if total_students else 0
    avg_dm_score = total_dm_score / total_students if total_students else 0
    
    return avg_python_score, avg_fsd_score, avg_dm_score

file_path = 'student.csv'
create_csv(file_path)

avg_python, avg_fsd, avg_dm = calculate_average(file_path)
print(f'Average Python Score: {avg_python}')
print(f'Average FSD Score: {avg_fsd}')
print(f'Average DM Score: {avg_dm}')