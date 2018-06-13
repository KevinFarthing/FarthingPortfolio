def calculator():
    input1 = input("Please input a number")
    input2 = input("Please input a number another number")
    if numcheck(input1) and numcheck(input2):
        return input1+input2
    else:
        print("Numbers only, Dammit")

def numcheck(num):
    return isinstance(num, int) or isinstance(num, float)

calculator()