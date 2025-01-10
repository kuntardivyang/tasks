class Library:
    
    @staticmethod
    def check_leap_year(year):
        if ((year%4==00 and year%100!=0) or (year%400==0)):
            print(year, 'Year is leap year. ')
        else:
            print(year, 'Year is not leap year. ')
    
Library.check_leap_year(1900)
Library.check_leap_year(2025)
