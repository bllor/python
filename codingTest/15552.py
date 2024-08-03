import sys

n = int(input())
for i in range(n):
    a,b = sys.stdin.readline().split(' ')
    a= int(a.rstrip())    
    b= int(b.rstrip())
    print(a+b)