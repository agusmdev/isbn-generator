import csv
from random import randint
from multiprocessing import Pool


def isValidISBN(isbn):

    # check for length
    if len(isbn) != 10:
        return False

    formatted_num = isbn.replace("-", "")

    """
    Computing weighted sum
    of first 9 digits
    """
    checksum = 0
    for i in range(9):
        digit = int(formatted_num[i])
        checksum += digit * (10 - i)

    """
    If last digit is 'X', add
    10 to sum, else add its value.
    """
    last = formatted_num[-1]
    checksum += 10 if last == 'X' else int(last)
    """
    Return true if weighted sum of
    digits is divisible by 11
    """
    return (checksum % 11 == 0)


def split_range(range_, n):
    div = range_//n
    res = [[0, div]]
    last_div = div
    for i in range(2, n):
        res.append([last_div, div*i])
        last_div = div*i
    return res


def multiprocess(limits=[]):
    start = limits[0]
    stop = limits[1]
    isbn_list = []
    for i in range(start, stop):
        isbn = str(i)
        isbn_ = "0"*(10 - len(isbn)) + isbn
        isbn_X = "0"*(9 - len(isbn)) + isbn + "X"
        if isValidISBN(isbn_):
            isbn_list.append(isbn_)
        if isValidISBN(isbn_X):
            isbn_list.append(isbn_X)
    return isbn_list


if __name__ == '__main__':
    isbns = []
    isbn_list = []

    args = split_range(1000000, 9)
    p = Pool(9)
    isbns += p.map(multiprocess, [*args])
    for i in isbns:
        isbn_list.extend(i)

    csvfile = "./isbns.txt"
    with open(csvfile, 'w') as resultFile:
        for i in isbn_list:
            resultFile.write(i + ",")
