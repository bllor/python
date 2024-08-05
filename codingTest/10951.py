'''
EOF error: 입력값이 없어서 발생한 에러
try~ except안에서 input()을 받으면 오류를 해결할 수 있다.
'''

a = True

while a:
    try:
        n,m = map(int, input().split(' '))
        print(n+m)
    except:
        break