# https://www.hackerrank.com/challenges/python-loops/problem

n = int(input())
if n < 1 and n > 20:
    n = 1
i = 0
while i < n:
    print (i**2)
    i = i + 1
