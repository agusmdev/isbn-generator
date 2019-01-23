import csv
from random import randint
from multiprocessing import Process, Pool



def isValidISBN(isbn):

    # check for length
    if len(isbn) != 10:
        return False
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




def multiprocess(limits=[]):
    start = limits[0]
    stop = limits[1]
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
    isbn_list = []
    args = [
            [0, 10000000],
            [10000000, 20000000],
            [20000000, 30000000],
            [30000000, 40000000],
            [40000000, 50000000],
            [60000000, 70000000],
            [70000000, 80000000],
            [80000000, 90000000],
            [90000000, 99999999],
            ]
    p = Pool(9)
    isbn_list += p.map(multiprocess, [*args])

    csvfile = "./isbns.txt"
    with open(csvfile, 'w') as resultFile:
        for i in isbn_list:
            for j in i:
                resultFile.write(j + ",")
