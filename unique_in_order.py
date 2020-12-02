iterable = 'AAAABBBCCDAABBB'
iterable = 'ABBCcAD'
iterable = [1, 2, 2, 3, 4]
iterable = [1]
iterable = 'AA'


def unique_in_oder(iterable):
    my_list = list(iterable)
    my_new_list = []
    if len(my_list) == 1:
        return my_list
    my_new_list.append(my_list[0])
    for index, c in enumerate(my_list[:-1]):
        if index < len(my_list)-1:
            if my_list[index+1] != c:
                print(c, '-t hasonlítom')
                print(my_list[index-1], '-el ')
                my_new_list.append(c)
    return my_new_list


# print(unique_in_order(iterable))
