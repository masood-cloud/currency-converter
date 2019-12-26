with open('currencydata.txt') as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]


amount = int(input("enter amount:\n"))
print("Enter name of the currency you want to convert this amount to? Available option :\n")
[print(item) for item in currencyDict.keys()]
currency = input("please enter one of its value\n")
print(f"{amount} pkr is equal to {amount * float(currencyDict[currency])} {currency}")
