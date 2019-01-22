from random import randint

isbn_list = []


def isValidISBN(isbn):

    # check for length
    if len(isbn) != 10:
        return False
    """
    Computing weighted sum
    of first 9 digits
    """
    _sum = 0
    for i in range(9):
        digit = int(isbn[i])
        _sum += digit * (10 - i)
    """
    If last digit is 'X', add
    10 to sum, else add its value.
    """

    _sum += 10 if isbn[9] == 'X' else int(isbn[9])
    """
    Return true if weighted sum of
    digits is divisible by 11
    """
    return (_sum % 11 == 0)


for i in range(9999999999):
    isbn = str(i)
    isbn_ = "0"*(10 - len(isbn)) + isbn
    isbn_X = "0"*(9 - len(isbn)) + isbn + "X"
    if isValidISBN(isbn_):
        isbn_list.append(isbn_)
    if isValidISBN(isbn_X):
        isbn_list.append(isbn_X)
