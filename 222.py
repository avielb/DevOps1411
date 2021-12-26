def print_x(size_of_x, what_to_print):
    for i in range(size_of_x):
        for j in range(size_of_x):
            if i + j == (size_of_x - 1) or i == j:
                print(what_to_print, end='')
            else:
                print(len(what_to_print) * " ", end='')
        print("")

print_x(10, "moshe")

for i in range(10):
    print("#"*(i + 1))