vowels = "aiuoeAOIEU"
s = str(input())
result = any(ch in vowels for ch in s)
if(result):
    print("Yes")
else:
    print("No")