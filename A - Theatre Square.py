n , m , a = map(int , input().split())

if n%a == 0 and m %a == 0 :
    print(n//a * m//a )
elif n%a == 0 or m%a == 0 :
    if n%a == 0 :
        print((n//a)*(m//a) + n//a)
    else :
        print((n//a)*(m//a) + m//a)
else :
    print((n//a) * (m//a)+ m//a + n//a + 1)
