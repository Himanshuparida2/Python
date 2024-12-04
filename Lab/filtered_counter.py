from collections import Counter
import matplotlib.pyplot as plt
st="""Fadnavis to be next CM, claims BJP leader: The name of Devendra Fadnavis has been finalised as the new chief minister of Maharashtra who will be elected as the legislature party leader in a meeting to be held either on December 2 or 3, news agency PTI quoted a senior BJP leader as saying on Sunday night. Earlier in the day, outgoing Chief Minister Eknath Shinde said he would support the BJP's decision to pick the new chief minister."""
count=Counter(st.split())
new_list=[(x,y) for x,y in count.items() if y>=3]
x=[]
y=[]

for (i,n) in new_list:
    x.append(i)
    y.append(n)
plt.bar(x,y)
plt.show()
