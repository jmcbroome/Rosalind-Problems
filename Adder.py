#Jakob McBroome
#BME 205

def adder(a,b):
    '''Adds all odd numbers in range A to B inclusive and returns the sum.'''
    output = 0
    for i in range(a,b+1):
        if i % 2 != 0:
            output += i
    return output

adder(100,200)

