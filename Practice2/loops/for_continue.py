for i in range(5):
    if i == 2:
        continue
    print(i) #0 1 3 4 




for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i) #1 3 5 7 9



arr = [3, -1, 5, 0, 7]
for x in arr:
    if x <= 0:
        continue
    print(x)  #3 5 7



#continue means:

#“Don’t do this step. Go to next.”


