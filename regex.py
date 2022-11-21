import re

pattern = r'^[+-]?\d*\.\d+$'
noOfInputs = int(input())
for i in range(1, noOfInputs + 1):
    number = input()
    result = re.search(pattern, number)
    print(bool(result))
