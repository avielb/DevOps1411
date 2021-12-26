my_file = open("read_my_contents.txt")
# print(list(my_file.readlines()))
for line in my_file.readlines():
    print(line, end='')

for name in ["shlomo", "david", "haim"]:
    print(name)

my_other_file = open("moshe.txt", "w")
my_other_file.write("hey hey\n")