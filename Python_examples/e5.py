!/usr/bin/python

def print_two(*args):
    arg1, arg2 = args
    print("Arg1 : {}, Arg2 : {}".format(arg1, arg2))

def print_two_again(arg1, arg2):
    print("Arg1 : {}, Arg2 : {}".format(arg1, arg2))

def print_one(arg1):
    print(f"Arg1 : {arg1}")

def print_none():
    print("Yo nigga what's up?")

print_two("Satan", "Lucifer")
print_two_again("Hail", "Satan")
print_one("Satan")
print_none()
