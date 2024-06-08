a = 9

n = 1
while n<=a:
    if str(n).endswith('3') or str(n).endswith('6') or str(n).endswith('9') :
        print("X", end=' ')
    else:
        print(n, end=' ')
    n+=1