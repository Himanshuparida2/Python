from datetime import date,timedelta
inp=input("Enter Todays Date (yyyy-mm-dd) : ")
DT=date.fromisoformat(inp)
n=int(input("Enter The no of days you want to add :"))
new_date=DT+timedelta(days=n)
Day=new_date.strftime('%A')
print(F"{new_date} and the day will be {Day}")
