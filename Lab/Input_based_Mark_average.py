total=0;
counter=0;
grade=int(input("Enter The Grade:,-1 to end: "))
while(grade!=-1):
    total+=grade
    counter+=1
    grade=int(input("Enter The Grade:,-1 to end: "))
if(counter==0):
    print("No Grades Were Entered")
else:
    print(f"Total Marks: {total}\nAvreage Mark: {total/counter:*^8.2f}")
