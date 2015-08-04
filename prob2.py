fibonacci = [1,2]
index = 1
newterm = 0
while True:
    newterm=fibonacci[index]+fibonacci[index-1]
    if newterm > 4000000:
        break
    fibonacci.append(newterm)
    index = index + 1 #generates fibonacci list
evens = []
for index in fibonacci:
    if index % 2 == 0:
        evens.append(index) #creates list of even fibonaccis
total = 0
for index in evens:
    total = total + index #adds contents of evens list to total
print total
