numbers = [1,2,3,4,5,6]
doubled = list(map(lambda x : x*2 ,numbers))
print(doubled)



words = ["hello","miras","what","is","your","name"]
upper = list(map(str.upper , words))
print(upper)



numbers = [1,5,7,8,9,6,4,1,2,3,68,45,26,95,74]
filtered_numbers = list(filter(lambda x : x%2==0,numbers))
print(filtered_numbers) 


words = ["apple","banana","pineapple","kaoa","owd"]
len_words = list(filter(lambda x : len(x)>4,words))
print(len_words)



words = ["apple","banana","pineapple","kaoa","owd"]
for i,word in enumerate(words):
    print(f"{i}:{word}")



names = ["Jack","Mike","Jone","Kate"]
for i,name in enumerate(names,start=1):
    print(f"{i}:{name}",end=" ")

print()

words = ["apple","banana","pineapple","kaoa","owd"]
for i,word in enumerate(words,start=1):
    print(f"{i}:{word}",end=" ")


print()

name = ["Jack","Mike","Jone","Kate"]
height = [125,541,546,1215]
for na,hei in zip(name,height):
    print(f"{na}'s height = {hei}")

pairs = list(zip(name,height))
print(pairs)

n,s = zip(*pairs)
print(list(n))
print(list(s))




number = [1,2,3,4,5,6,7,8,9]
print(sorted(number))
print(sorted(number,reverse=True))



words = ["wleijbi3","iu iyu2 3giyu r","2i3iuwgiuygt","wierb"]
print(sorted(words,key=len))
print(sorted(words,key=len,reverse=True))



for x in reversed([1,2,3]):
    print(x,end=" ")#3 2 1



nums = [2,4,8,7,10]
print(any(x%2!=0 for x in nums))
print(all(x%2==0 for x in nums))



word = ["banana","kiwi","apple"]
print(min(word,key=len))
print(max(word,key = len))



print(sum([1,2,3,4,5,6,7,8,9,10]))
print(sum([1,2,3,4,5,6,7,8,9,10],start = 10))


names  = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
grades = [85, 55, 72, 48, 91]
passed = []
for name,grade in zip(names,grades):
    if(grade >= 60):
        passed.append(name)
result = list(map(lambda x : x.upper() , passed))
print(result)





prices = [499.99, 1200.00, 350.50, 2500.00, 899.99, 1050.00]
for i,pr in enumerate(prices,start = 1):
    print(f"{i}.{pr:.2f}")
expensive = list(filter(lambda p : p>1000,prices))
print(f"Expensive items:{expensive}")
print(f"Total: {sum(expensive):.2f}")




a = [(1, 2), (2, 3), (1, 1), (2, 2), (4, 5)]
b = sorted(a)
print(b)



f = open("input.txt","r")
