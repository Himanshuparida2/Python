class Point:
                def __init__(self,x,y):
                                self.x=x
                                self.y=y
                def __add__(self,other):
                                """
                                >>> p1=Point(2,3)
                                >>> p2=Point(1,3)
                                >>> p1+p2
                                Point(3,6)
                                """
                                return Point(self.x+other.x,self.y+other.y)
                def __repr__(self):
                                return f'Point({self.x},{self.y})'
if __name__ == '__main__':
                import doctest
                doctest.testmod()
