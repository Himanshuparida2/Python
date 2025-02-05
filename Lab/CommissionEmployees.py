class Commission_Employee(object):
                def __init__(self,FirstName,LastName,ssn,gross_sales,Commission_Rate):
                                self.FirstName=FirstName
                                self.LastName=LastName
                                self.ssn=ssn
                                self.gross_sales=gross_sales
                                self.Commission_Rate=Commission_Rate
                @property
                def gross_sales(self):
                                return self._gross_sales
                @gross_sales.setter
                def gross_sales(self,value):
                                if value<0:
                                                raise ValueError('Gross Sales cannot be Negative.')
                                self._gross_sales=value
                @property
                def Commission_Rate(self):
                                return self._Commission_Rate
                @Commission_Rate.setter
                def Commission_Rate(self,value):
                                if not(0<value):
                                                raise ValueError('Commission Rate must be 0-1.')
                                self._Commission_Rate=value
                def earning(self):
                                return self.gross_sales*self.Commission_Rate
                def __str__(self):
                                return f'Commission Employee : \n{self.FirstName} {self.LastName}\nSSN : {self.ssn}\nEarning : {self.earning()}'
