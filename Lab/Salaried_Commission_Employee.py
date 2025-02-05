from CommissionEmployees import Commission_Employee as CommissionEmployee
class SalariedCommissionEmployee(CommissionEmployee):
                def __init__(self,FirstName,LastName,ssn,gross_sales,Commission_Rate,base_salary):
                                super().__init__(FirstName,LastName,ssn,gross_sales,Commission_Rate)
                                self.base_salary=base_salary
                @property
                def base_salary(self):
                                return self._base_salary
                @base_salary.setter
                def base_salary(self,value):
                                if value<0:
                                                raise ValueError('Base Salary cannot be Negative.')
                                self._base_salary=value
                def earning(self):
                                return super().earning()+self.base_salary
                def __str__(self):
                                return super().__str__()+f"\nBase Salary : {self.base_salary}"
                                
