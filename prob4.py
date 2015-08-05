def ispalindrome(number):
    number = str(number) #strs are easier to reverse
    revnumber = ""
    for digit in number[::-1]:
        revnumber = revnumber + digit #loops through and adds each digit to revnumber
    if number == revnumber:
        return True
    else:
        return False

def multnumbers():
    product = 0
    palin = []
    for x in range(999,99,-1):
        for y in range(999,99,-1): #these loops multiply every combination of #s from 100-999
            product = x*y
            if ispalindrome(product) == True:
                palin.append(product) #each palindrome result is added to a list...
    print max(palin) #and the highest one is printed

multnumbers()
