import matplotlib.pyplot as plt
from random import random as r
dic={"ABC":1,"BCW":5,"WWE":4}
x=list(dic.keys())
y=list(dic.values())
colour=[tuple(r() for _ in range(3)) for _ in range(len(x))]
plt.bar(x,y,color=colour)
plt.xlabel("Word")
plt.ylabel("frequency")
plt.title("Word Count Bar Chart")
for i,y in enumerate(y):
    plt.text(i,y+0.05,f"{y}")
plt.show()
