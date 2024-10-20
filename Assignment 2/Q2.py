'''2. Write a program such that Python will ask you if it is raining or not. 
If your answer is ”yes”, Python will say ”Carry an umbrella”. 
If you say ”no”, Python will say ”No need to carry an umbrella”.
If you type anything else, Python will say ”Bye”.'''

inp=input("Is It Raining?")
if(inp=="yes" or inp=="YES" or inp=="Yes"):
    print("Carry a umbrella")
elif(inp=="No"):
    print("No need to carry an umbrella")
else:
    print("Bye")