#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_value = max(a_dictionary.values())
        for key in a_dictionary.keys():
            if a_dictionary[key] == max_value:
                return key
            else:
                continue
    else:
        return None


if __name__ == "__main__":
    best_score(a_dictionary)
