grades=[98,76,71,87,83,90,57,79,82,94]
total=0;
counter=0;
for g in grades:
    total+=g;
    counter+=1
print(f"Average Marks: {total/counter:*^7.2f}")
