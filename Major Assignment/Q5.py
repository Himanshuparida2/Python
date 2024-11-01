from Q1 import basic_salary
from Q2 import tax_amount
from Q3 import gross_salary
from Q4 import salary_bracket

def employee_report():
    count=0
    while(True):
        name=input("Enter the Employee Name : ")
        hours=int(input(F"Enter {name}'s Work Hours per week : "))
        hourly_rate=int(input(F"Enter {name}'s Hourly Rate : "))
        basic=basic_salary(hourly_rate,hours)
        tax=tax_amount(basic)
        gross=gross_salary(basic,tax)
        salary=salary_bracket(gross)
        print(F"\nEmployee Name: {name}\nBasic Salary: {basic}\nGross Salary: {gross}\nTax Amount: {tax}\nSalary Bracket: {salary}\n")
        count+=1
        if(count==3):
            break

employee_report()