def pop(list):
    def get_last_item(my_list):
        # usuwa ostatni element z listy otrzymany przez zewnętrzną funkcję
        return my_list[len(list) - 1]

    # usuwa ostatni element listy
    list.remove(get_last_item(list))

    # zwraca liste
    return list

test_list = [1,2,3,4,5]
print(pop(test_list))
print(pop(test_list))
print(pop(test_list))
print(pop(test_list))