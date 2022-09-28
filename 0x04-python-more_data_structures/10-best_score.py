#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    else:
        keys = sorted(a_dictionary.keys())
        for i in keys:
            max = a_dictionary[keys[0]]
            if a_dictionary[i] >= max:
                max = a_dictionary[i]
            else:
                return max
    for i in a_dictionary:
        if a_dictionary[i] == max:
            return i
