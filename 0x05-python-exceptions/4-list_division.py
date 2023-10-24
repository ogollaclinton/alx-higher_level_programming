#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    a = 0
    list_master = []
    while a < list_length:
        b = 0
        try:
            b = my_list_1[a] / my_list_2[a]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            list_master.append(b)
            a += 1
    return list_master
