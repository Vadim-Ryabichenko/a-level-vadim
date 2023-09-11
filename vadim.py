from typing import Union


def is_palindrome(origin: Union[str, int], /) -> bool:

    punct = ('.', '?', '!', ':', ';', '-', '—', ' ',)
    origin = str(origin)
    for symbol in punct:
        if symbol in origin:
            origin = origin.replace(symbol, "")

    return origin.lower() == origin.lower()[::-1]

assert is_palindrome("aba") is True
assert is_palindrome("abc") is False
assert is_palindrome(12345) is False
assert is_palindrome(12321) is True



def get_longest_palindrome(origin: str, /) -> str:

    max_pal_1 = ""
    max_pal_len_1 = 0
    max_pal_2 = ""
    max_pal_len_2 = 0

    for i in range(len(origin)):
        left = i
        right = i
        while left >= 0 and right < len(origin) and origin[left] == origin[right]:
            if right - left > max_pal_len_1:
                max_pal_1 = origin[left:right + 1]
                max_pal_len_1 = len(max_pal_1)
            left -= 1
            right += 1
        for j in range(len(origin)):
            left = j
            right = j + 1
            while left >= 0 and right < len(origin) and origin[left] == origin[right]:
                if right - left > max_pal_len_2:
                    max_pal_2 = origin[left:right + 1]
                    max_pal_len_2 = len(max_pal_2)
                left -= 1
                right += 1
    if max_pal_len_1 > max_pal_len_2:
        return max_pal_1
    else: return max_pal_2

assert get_longest_palindrome("0123219") == "12321"
assert get_longest_palindrome("1012210") == "012210"



def are_parentheses_balanced(origin: str, /) -> bool:

    list_backets = []

    for i in origin:
        list_backets.append(i)

    if list_backets.count("[") == list_backets.count("]") and list_backets.count("(") == list_backets.count(
            ")") and list_backets.count("{") == list_backets.count("}"):

        index = 0

        while len(list_backets) != 0:

            if list_backets[index] == "(" and list_backets[-1] == ")" or list_backets[index] == "{" and list_backets[
                -1] == "}" or list_backets[index] == "[" and list_backets[-1] == "]":
                list_backets.pop(index)
                list_backets.pop(-index - 1)
            else:
                break

    if (len(list_backets)) == 0:
        return True
    else:
        return False

assert are_parentheses_balanced("({[]})") is True
assert are_parentheses_balanced(")]}{[(") is False




def get_longest_uniq_length(origin: str, /) -> int:

    empty_s = ""
    result = 0

    for i in origin:
        if i not in empty_s:
            empty_s += i
            result = max(result, len(empty_s))
        else:
            next_seq = empty_s.index(i)
            empty_s = empty_s[next_seq + 1:] + i

    return result

assert get_longest_uniq_length("abcdefg") == 7
assert get_longest_uniq_length("racecar") == 4
