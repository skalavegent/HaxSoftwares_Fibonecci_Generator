n = int(input("Hi, How many numbers do you wish to have in this series: "))
a = 0
b = 1

for i in range(n):
    print(a)
    x = a
    a = b
    b = x + b