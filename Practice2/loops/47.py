a = int(input())
d = dict()
for _ in range(a):
    key , value = input().split()
    d[key] = value
    value = int(value)
for key in d:
    d[key]+=value
for key in sorted(d):
    print(key , d[key])