#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    sublist = list()
    division = 0
    for num in range(list_length):
        try:
            division = my_list_1[num] / my_list_2[num]
        except IndexError:
            print("Out of range")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except TypeError:
            print("wrong type")
            division = 0
        finally:
            sublist.append(division)
    return sublist
