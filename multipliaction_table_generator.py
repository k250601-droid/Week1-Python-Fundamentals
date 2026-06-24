num = int(input("Enter a number: "))
limit = int(input("Enter limit: "))

for i in range(1, limit + 1):
    print(f"{num} x {i} = {num * i}")