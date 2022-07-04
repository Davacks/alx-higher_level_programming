#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sublist in matrix:
        for i in range(len(sublist)):
            print("{:d}".format(sublist[i]), end="")
            if i is not len(sublist) - 1:
                print(" ", end="")
        print("")


if __name__ == "__main__":
    print_matrix_integer(matrix)
