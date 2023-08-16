#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = list()
    for lists in my_list:
        if lists == search:
            lists = replace
        newList.append(lists)
    return newList
