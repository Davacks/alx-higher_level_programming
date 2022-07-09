#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary)
    for i in range(0, len(sorted_keys)):
        print('{}: {}'.format(sorted_keys[i], a_dictionary[sorted_keys[i]]))


if __name__ == "__main__":
    print_sorted_dictionary(a_dictionary)
