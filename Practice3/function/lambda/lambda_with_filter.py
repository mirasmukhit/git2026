words = ["cat", "elephant", "dog", "giraffe"]
long_words = list(filter(lambda w: len(w) > 4, words))
print(long_words) #Filter strings longer than 4 letters




students = [
    {"name": "Ali", "score": 85},
    {"name": "Sara", "score": 45},
    {"name": "Tom", "score": 70}
]
passed = list(filter(lambda s: s["score"] >= 60, students))
print(passed)











