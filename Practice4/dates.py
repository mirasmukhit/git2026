import datetime
x = datetime.datetime.now()
print(x)#2026-02-27 19:22:02.800495




import datetime
x = datetime.datetime.now()
print(x.year)#2026
print(x.strftime("%A"))#Friday



import datetime
x = datetime.datetime(2020, 5, 17)
print(x)



from datetime import datetime,timedelta
n  = datetime.now()
print(n + timedelta(minutes = 60))





from datetime import datetime,timedelta
a = datetime(2026,12,30,15,30,00)
b = datetime(2026,12,29,15,00,00)
diff = a - b
print(diff)
print(diff.days)
print(diff.total_seconds)