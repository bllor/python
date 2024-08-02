h,m = [23, 48]
t = 70

ah = t//60
am = t-ah*60


if am+m>=60:
    if h+ah>=23:
        print(h+ah-23,am+m-60)
    else:
        print(h+ah+1,am+m-60)
else:    
    if h+ah>=24:
        print(h+ah-24,am+m)
    else:
        print(h+ah,m+am)