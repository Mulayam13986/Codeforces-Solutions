n , k = map(int ,input().split())
list1 = list(map(int , input().split()))
count = 0 
list1.sort(reverse=True)
for i in list1 :
    if i >= list1[k-1] and i > 0:
        count+=1
print(count)