'''3. Write a Python program to calculate a student’s letter grade based on their numeric score using the following scale:- 
A (90–100), B (80–89), C (70–79), D (60–69), and F (below 60). 
Additionally, provide a comment for each grade: ”Excellent” for A, ”Good” for B, ”Average” for C, ”Needs Improvement” for D, and ”Failing” for F.'''

def Grade(i):
    if(i>=90 and i<=100):
        print("Excellent")
        return 'A'
    elif(i>=80 and i<=89):
        print("Good")
        return 'B'
    elif(i>=70 and i<=79):
        print("Average")
        return 'C'
    elif(i>=60 and i<=69):
        print("Need Improvement")
        return 'D'
    elif(i<60):
        print("Failing")
        return 'F'
    else:
        return 'Invalid Input Try Again'

inp=int(input("Enter Your Score: "))
K=Grade(inp)
print(K)
