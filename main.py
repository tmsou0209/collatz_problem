import sys
from matplotlib import pyplot

list = []
list.append(int(sys.argv[1],10))

num = list[len(list)-1]

while num!=1:
    if num%2==1:
        num=num*3+1
    else:
        num/=2
    list.append(num)
    print(num)

print(len(list))

pyplot.plot(range(0,len(list)), list) 
pyplot.show()