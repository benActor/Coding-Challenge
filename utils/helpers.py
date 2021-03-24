
"""
    Some Set up functions to improve code readability
"""

# returns the first element of a list
first_of = lambda tree: tree[0]

# returns the list without the first element
rest_of = lambda tree: tree[1:]


def el_count(el, l):
    """
    :param el: an element to count occurences
    :param l: list of element to check for occurrences
    :return:
    """
    if l == []:
        return 0
    elif first_of(l) == el:
        return 1 + el_count(el, rest_of(l))
    else:
        return el_count(el, rest_of(l))


def has_same_elements(x, y):
    """
    Check if list x and y are combination
    :param x: a list
    :param y: another list
    :return: boolean if both lists are combination
    """
    for i in x:
        if i not in y or el_count(i, x) != el_count(i, y):
            return False
    return True


def contains_combination(entry, nested_list):
    """

    :param entry: a simple list [1, 2, 3, 4]
    :param nested_list: a nested list [[1, 3, 4, 6], [2, 4, 8, 3], [4, 1, 2, 3]]
    :return: boolean if entry contains combination of entry
    """
    if nested_list == []:
        return False
    elif has_same_elements(entry, first_of(nested_list)):
        return True
    else:
        return contains_combination(entry, rest_of(nested_list))


def drop_duplicates(nested_list):
    """
    drop the duplicates in a nested list

    :param nested_list: a nested list [[1, 3, 4, 6], [2, 4, 8, 3], [4, 1, 2, 3]]
    :return: nested list without duplicates combination  [[[1, 3, 4, 6], [2, 4, 8, 3]]
    """
    if nested_list == []:
        return []
    elif contains_combination(first_of(nested_list), rest_of(nested_list)):
        return drop_duplicates(rest_of(nested_list))
    else:
        return [first_of(nested_list)] + drop_duplicates(rest_of(nested_list))


def append_elements_with_v(v, list_elt):
    """

    :param v: value E
    :param list_elt: [1, 1, 3, 4, 5]
    :return: [['E', 1], ['E', 1], ['E', 3], ['E', 4], ['E', 5]]
    """
    if list_elt == []:
        return []
    else:
        return [[v, first_of(list_elt)]] + append_elements_with_v(v, rest_of(list_elt))


# print(append_elements_with_v(1, [1, 1, 3, 4, 5]))

def app_val_nested_list(nested_list, v):
    """

    :param nested_list: [[1, 1], [1, 3], [1, 4], [1, 5], [1, 3], [1, 4], [1, 5], [3, 4], [3, 5], [4, 5]]
    :param v: 3
    :return: [[3, 1, 1], [3, 1, 4], [3, 1, 5], [3, 1, 4], [3, 1, 5], [3, 4, 5]]
    """
    if nested_list == []:
        return []
    elif v in first_of(nested_list):
        return app_val_nested_list(rest_of(nested_list), v)
    else:
        return [[v] + first_of(nested_list)] + app_val_nested_list(rest_of(nested_list), v)



def combine_two_sets(entry_list, nested_list):
    """

    :param entry_list: [1, 1, 3, 4, 5]
    :param nested_list: [[1, 1], [1, 3], [1, 4], [1, 5], [1, 3], [1, 4], [1, 5], [3, 4], [3, 5], [4, 5]]
    :return: [[3, 1, 1], [4, 1, 1], [4, 1, 3], [5, 1, 1], [5, 1, 3], [5, 1, 4], [5, 3, 4]]
    """
    if entry_list == []:
        return []
    else:
        return drop_duplicates(app_val_nested_list(nested_list, first_of(entry_list)) +
                               combine_two_sets(rest_of(entry_list), nested_list))


def combination_of_2_in_list(list_value):
    """

    :param list_value: [1, 2, 3, 4, 5]
    :return: [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]
    """
    if list_value == []:
        return []
    else:
        return drop_duplicates(append_elements_with_v(first_of(list_value), rest_of(list_value)) +
                               combination_of_2_in_list(rest_of(list_value)))



def combination_of_n(list_value, n):
    """

    :param list_value:  [1, 2, 3, 4, 5]
    :param n: 3
    :return:
    """
    if n == 0:
        return []
    elif n == 1:
        return [[x] for x in list_value]

    elif n == 2:
        return combination_of_2_in_list(list_value)
    else:
        return combine_two_sets(list_value, combination_of_n(list_value , n-1))


def all_n_combinations(list_value):
    """

    :param list_value: [1, 2, 3, 4]
    :return: [[1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [3, 1, 2], [4, 1, 2], [4, 1, 3],
    [4, 2, 3], [4, 3, 1, 2]]
    """
    result = []
    for n in range(len(list_value) + 1):
        result += combination_of_n(list_value, n)
    return result