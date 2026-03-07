import re

input_path = r"C:\Users\Miras\Documents\githowto\githowto\files\Practice 05\raw.txt"
output_path = r"C:\Users\Miras\Documents\githowto\githowto\files\Practice 05\output.txt"

outputer = ""

with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()

total_amount = 0

# Prices
prices = re.findall(r"Стоимость\s*\n\s*([\d ]+)", text, flags=re.MULTILINE)

outputer += "_" * 100 + "\n"
outputer += "Prices of Products\n"

for p in prices:
    outputer += p + "\n"

# Product names
names = re.findall(r"\d+\.\n(.+)", text, flags=re.MULTILINE)

outputer += "-" * 100 + "\n"
outputer += "---------Names of products----------\n"

for n in names:
    outputer += n + "\n"

# Total amount by adding all prices
for p in prices:
    parts = p.split()
    if len(parts) > 1:
        total_amount += int(parts[0]) * 1000 + int(parts[1])
    else:
        total_amount += int(parts[0])

outputer += "-" * 100 + "\n"
outputer += f"Total amount = {total_amount:.2f} тг\n"

# Date and time
times = re.findall(r"Время:\s*(\d+\.\d+\.\d+ \d+:\d+:\d+)", text)

for tm in times:
    outputer += "Date and Time: " + tm + "\n"

# Operator / payment line
operators = re.findall(r"Оператор фискальных данных:\s*(.+)", text)

for op in operators:
    outputer += "Operator: " + op + "\n"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(outputer)