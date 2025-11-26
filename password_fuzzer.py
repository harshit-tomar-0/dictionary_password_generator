#python3
#random password fuzzer
from random import choice
example_words=["harsh","sharma","01031956","mumbai","iitbombay"]
import string
example_limit=8
temp=None
new_example=[]
for i in example_words:
    temp=int(example_limit/2)
    if len(i)>temp+1:
        new_example.extend(i.partition(i[temp:temp+1]))
    else:
        ...
print(new_example)
for i in range(0,len(new_example)):
    symbol=choice(list(string.punctuation))
    for j in range(0,len(new_example)):
        temp=new_example[i]+symbol+new_example[j]
        if len(temp)<=8:
            print("::",temp)
        else:
            print("%",temp)
