isTrue = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"

if a >= 2 and (strOne == "One" or not strThree == "two"):
    print("a is greater then 2")
elif b == 2.5 or b == 2.5:
    print("something")
elif strOne == "3":
    print("bla")
else:
    print("a is lower then 2")

my_list = ["hen", "lior", "shay", "ariel"]
my_other_list = []
if 0 < a <= 4:
    print("ok ")

if "hen" in my_list:
    print("we have found hen!")

if my_other_list:
    print("hello")

if len(my_other_list) > 0:
    print("hey")

c = ["aaa", "1"]
d = ["aaa", "1"]
e = 9.0
if c is d:
    print("c is d")

if type(e) is int:
    print("e is an integer")
