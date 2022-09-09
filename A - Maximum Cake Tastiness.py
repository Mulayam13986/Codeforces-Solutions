t = int(input())
for i in range(t) :
    a = int(input())
    list1 = list(map(int , input().split()))
    list1.sort()
    print(list1[a-1] + list1[a-2])