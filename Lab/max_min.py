n1=float(input("Enter First Number:"))
n2=float(input("Enter Second Number:"))
n3=float(input("Enter Third Number:"))
maximum=max(n1,n2,n3)
minimum=min(n1,n2,n3)
mid=n1+n2+n3-maximum-minimum
print(maximum,mid,minimum)
