class Vector:
                def __init__(self,*components):
                                self.component=components
                def __add__(self,other):
                                return Vector(*[x+y for x,y in zip(self.component,other.component)])
                def __mul__(self,other):
                                return Vector(*[x*other for x in self.component])
                def __sub__(self,other):
                                return Vector(*[x-y for x,y in zip(self.component,other.component)])
                def __repr__(self):
                                return f'Vector({self.component})'
