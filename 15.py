what_to_print = "hello world!"
list_of_names = ["hen", "michael", "noam", "lior", "amichai"]
amount_of_prints = 4
for i in range(1, amount_of_prints):
    print(str(i) + ") " + what_to_print)

for i in range(len(list_of_names)):
    print(list_of_names[i])

for name in list_of_names:
    if name == "hen":
        continue
    print(name)

# a = 0
# while a < 10:
#     print(a)
#     a = a + 1

for i in range(1, 101):
    if i % 7 != 0 and "7" not in str(i):
        print(i)

a = "a"
while a != "q":
    a = input("enter q or not: ")

else:
    print("finished successfully", end='')

if i in range(5):
    print(i)
else:
    print("finished successfully")
