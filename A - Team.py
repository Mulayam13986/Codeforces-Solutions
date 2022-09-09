a = int(input())
count = 0 
for i in range(a) :
    list1 = list(map(int , input().split()))
    t = sum(list1)
    if t >= 2 :
        count +=1 

print(count)
