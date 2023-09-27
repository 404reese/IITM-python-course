str = input()
numbers = str.split(',')
product = 1

for num in numbers:
    num = int(num)
    product *= num
print(product)