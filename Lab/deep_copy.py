import copy
L=['a',1,"abc",[i for i in range(1,11)]]
deep_copy=copy.deepcopy(L)
print(deep_copy,"\n After Deep Copy and some changes in deep copy")
deep_copy[3][2]="Z"
print(deep_copy,'\n The Original List')
print(L)
