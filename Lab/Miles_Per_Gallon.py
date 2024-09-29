gallons=0
total_mile=0
total_gal=0
while(gallons!=-1):
    gallons=float(input("Enter The gallons used(-1 to end) : "))
    if(gallons==-1):
        break
    miles=float(input("Enter the Miles Driven : "))
    print(f"The Miles/Gallon for this tank was {miles/gallons:4.2f}")
    total_mile+=miles
    total_gal+=gallons
if(total_mile==0):
    print("No miles were Driven")
else:
    print(f"Total Mileage Per Gallon is {total_mile/total_gal}")
