def funcA(n):
                print(f"FuncA {n}")
                n-=1
                if(n==0):
                                return
                funcB(n)
def funcB(n):
                print(f"FuncB {n}")
                n-=1
                if(n==0):
                                return
                funcA(n)
n=10
funcA(n)
