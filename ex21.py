def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def sub(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b
   
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(20, 4)
hieght = sub(78, 4)
weight = multiply(140, 2)
iq = divide(100, 2)

print(f"Age: {age}, hieght: {hieght}, wight: {weight}, iq: {iq}.")


print("Here is a puzzle")

what = add(age, sub(hieght,multiply(weight, divide(iq, 2))))

print("That becomes", what, "Can you do it by hand?")