def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(4, 5)
print_params(1)
print_params(1, 3, 4)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, "2", None]
values_dict = {"a": 1, "b" : "2", "c" : None}
print_params(*values_list)
print_params(**values_dict)
values_list2 = [2, None]
print_params(*values_list2, 42)


