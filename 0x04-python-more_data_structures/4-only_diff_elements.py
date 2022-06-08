#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = []
    for a in set_1:
        for b in set_2:
            if a != b:
                set_3.append(a)
    return set_3
