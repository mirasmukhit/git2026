n = int(input())
arr  = list(map(str , input().split()))
d = dict()
for i in arr:
    if i not in d:
        d[i]=0
    d[i]=d[i]+1
for key in d:
    print(key , d[key])