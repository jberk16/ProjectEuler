ints = [x for x in range(1000) if x % 3 == 0 or x % 5 == 0]
sum = 0
for index in ints:
    sum = sum + index
print sum
