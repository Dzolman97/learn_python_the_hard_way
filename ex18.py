# like using scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# that args is pointless we can make it smaller
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# take one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# take no arguments
def print_none():
    print("I got nothin.")


# call functions

print_two("Daniel", "Zolman")
print_two_again("Dan", "The Man")
print_one("First!")
print_none()