a = (2,5,4,8,9,1,7)
result = sorted(a,key=lambda x:abs(x))
print(result)







sozder = ['banana','apple','cheery','mango']
result = sorted(sozder,key=lambda x:len(x))
print(result)





students = [
    {"name": "Ali", "score": 85},
    {"name": "Sara", "score": 92},
    {"name": "Tom", "score": 78}
]
result = sorted(students, key=lambda s: s["score"])
print(result)
