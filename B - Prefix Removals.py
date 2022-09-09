for i in range(int(input())):
    a=input()
    i=0
    while a[i] in a[i+1:]:
        i+=1
    print(a[i:])