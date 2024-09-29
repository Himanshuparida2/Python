passes=0
failures=0
for g in range(10):
    result=int(input("Enter Your Result: "))
    while(result<0 and result>100):
        print("Invalid Input")
        result=int(input("Enter Your Result: "))
    if(40<=result):
        failures+=1
    else:
        passes+=1
print(f"Total Passes: {passes} Total Failures: {failures}")
if passes>8:
    print("Bonus For The Instructor.")
