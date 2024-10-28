from datetime import timedelta,date
new_date=date.today() + timedelta(days=5)
print(new_date)
print(F"and the Day is {new_date.strftime('%A')}")
