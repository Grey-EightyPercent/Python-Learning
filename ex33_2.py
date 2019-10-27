numbers = []

for i in range(0, 6):
    print(f"At the top i is {i}")
    numbers.append(i)
    print("Numbers now: ", numbers)
    i = i + 1 # 这里i是否被赋值无所谓，因为在for i range(0, 6)都会被刷新
    print(f"At the bottom i is {i}")

print("The numbers:")
for num in numbers:
    print(num)
