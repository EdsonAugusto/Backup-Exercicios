from math import sqrt
def find_next_square(sq):
    if type(sqrt(sq)) != int:
        return -1
    else:
        sq += 1
        while type(sqrt(sq)) != int:
            if sqrt(sq) == int:
                return sq
            else:
                sq += 1

print(find_next_square(121))