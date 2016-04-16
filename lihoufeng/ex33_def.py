global numbers
numbers = []

def mywhile(numebrs, step):
    i = 0
    while i < 6:
        print "At the top i is %d" % i
        numbers.append(i)

        i += step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

mywhile(numbers, 1)

print "The numbers: "

for num in numbers:
    print num
