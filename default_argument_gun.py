def combine_reversed(list1, list2=[]):
    list2.extend(list1)
    return list2


if __name__ == '__main__':
    print(combine_reversed([1]))
    print(combine_reversed([2], [3]))
    print(combine_reversed([]))