#! /usr/bin/env python3
n = 1000 

# fizzbuzz game 
# count from 1 to n
for i in range(n+1):
    if i % 3 ==0 and i % 5 ==0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
    
# if the number is divisible by 3, say fizz
# if the number is divisible by 5, say buzz 
# if the number is divisible by both, say fizzbuzz


