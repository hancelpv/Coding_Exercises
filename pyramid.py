list_of_num = range(1, 9)
spacer = len(list_of_num)
print("Spacer : {}".format(spacer))
for index in range(1, len(list_of_num)):
    sublist = [str(x) for x in list_of_num[:index]]
    num_string = ' '.join(sublist)
    print(" " * spacer + num_string)
    spacer -= 1
