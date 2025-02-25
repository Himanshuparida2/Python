class point:
                def __init__(self,x,y):
                                self.x=x
                                self.y=y
                def __add__(self,other):
                                return point(self.x+other.x,self.y+other.y)
                def distance(self):
                                return (self.x**2 + self.y**2)**0.5
                def __eq__(self,other):
                                return self.distance()==other.distance()
                def __lt__(self,other):
                                return self.distance()<other.distance()
                def __repr__(self):
                                return f'P({self.x},{self.y})'
