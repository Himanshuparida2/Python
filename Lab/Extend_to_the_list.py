Colours=['orange','green','blue']
print(Colours)
while(True):
    c=[input("Enter the List you want to add to the exising List (press n to exit): ")]
    if('n' in c):
        break
    Colours.extend(c)
print(Colours)
