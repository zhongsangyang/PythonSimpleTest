#!/usr/bin/env python
# -*- encoding:UTF-8 -*-
fruits=['banana','fruit','watermelon','orange'];
for i in range(len(fruits)):
    print("我是当前的水果",fruits[i]);
for num in range(10,20):#迭代10,20之间的数字
    for i in range(2,num):
        if num%i==0:
            j=num/i;
            print ('{0} 等于 {1} * {2}'.format(num, i,j));
            break;
    else:
        print("{0}是个质素".format(num));
for i,j in enumerate(fruits):
    print(j); 
print("-----------------"); print("{0[0]}".format(fruits));
