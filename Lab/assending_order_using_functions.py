def assending_order(a,b,c):
    mini=min(a,b,c)
    maxi = max(a,b,c)
    return mini,(a+b+c)-(maxi+mini),maxi
print(assending_order(1,2,3))
