from datetime import date
input_date = input("Input a date in the format dd-mm-yyyy: ")
day, month, year = map(int, input_date.split("-"))

dob = date(year, month, day)
today = date.today()


age = today.year - dob.year
if ((today.month, today.day) < (dob.month, dob.day)):
    age -= 1

print(age)
