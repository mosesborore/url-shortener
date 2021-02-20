import unittest
import string

BASE62LETTERS = list(string.digits + string.ascii_letters)

def base62_encode(num: int):
    """
        @param num: number to convert to its base62 equivalent
    """
    if num <= 61:
        return BASE62LETTERS[num]
    else:
        result = []

        while num > 0:
            reminder = num % 62

            temp = BASE62LETTERS[reminder]
            result.append(str(temp))
            num //= 62

        result.reverse()

        return "".join(result)

def base62_decode(s: str):
    """
        @param s: string to convert to its base10 equivalent
    """
    s = list(s)
    s.reverse()

    res = []
    for i in range(len(s)):
        # if the item at i
        # is digit: 0-9, ascii_letters: a-z A-Z
        if s[i] in BASE62LETTERS:
            res.append(BASE62LETTERS.index(s[i]) * (62**i))
        else:
            temp = int(s[i]) * (62**i)
            res.append(temp)

    return sum(res)

if __name__ == '__main__':
    print(base62_encode(100))
