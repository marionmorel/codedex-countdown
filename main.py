# Import daytime module and bday_message
import datetime
import bday_message

# Create two date objects with the daytime module
today = datetime.date.today()
next_birthday = datetime.date(2024, 9, 10)

# Calculate how many days away from today is next_birthday
days_away = next_birthday - today

# Create a control flow statement
if today == next_birthday:
    print(bday_message)
else:
    print(f'My next birthday is {days_away.days} days away!')

# Calculate how many days, months and years it has been since you were born
birth_date = datetime.date(1997, 9, 10)

days_since = today - birth_date
years_since = round(days_since.days / 366)
months_since = years_since * 12

print(f'I was born {days_since.days} days, {months_since} months and {years_since} years ago!')