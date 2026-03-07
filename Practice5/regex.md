import re
text = input("Enter a string: ")
pattern = r"^ab*$"
    if re.fullmatch(pattern, text):
    print("Matched")
else:
    print("Not matched")




import re
s = input()
if refullmatch(r"^ab{2,3}$",s):
    print("Matched")
else:
    print("Not matched")





import re
s = input()
print(list(re.findall("[a-z]",s)))




import re
s=input()
print(*list(re.findall("[A-Z](?=[a-z])",s)))








import re 
s = input()
if re.fullmatch(r"[a].*[b]$",s):
    print("Matched")
else:
    print("Not matched")







import re
s = input()
print(re.sub(r"[ ,.]", ":", s))






s = input()
parts = s.split("_")
camel = parts[0] + "".join(word.capitalize() for word in parts[1:])
print(camel)






import re
s = input()
print(re.split(r"(?=[A-Z])", s))





import re
s = input()
print(re.sub(r"(?<!^)([A-Z])", r" \1", s))







import re
s = input()
print(re.sub(r"([A-Z])", r"_\1", s).lower())