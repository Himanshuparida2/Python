def basic_salary(hourly_rate,hours_worked_per_week):
    if(hours_worked_per_week>40):
        return hourly_rate*40
    else:
        return hourly_rate*hours_worked_per_week

def overtime_salary(n,hourly_rate):
    return n*(hourly_rate*1.5)

def total_salary(hourly_rate,hours_worked_per_week,tax):
    if(hours_worked_per_week>40):
        return overtime_salary(hours_worked_per_week-40,hourly_rate)+basic_salary(hourly_rate,hours_worked_per_week)-tax
    else:
        return basic_salary(hourly_rate,hours_worked_per_week)