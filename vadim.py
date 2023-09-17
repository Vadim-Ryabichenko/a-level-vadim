from typing import Union


def is_palindrome(origin: Union[str, int], /) -> bool:

    punct = (".", "?", "!", ":", ";", "-", "—", " ", "/", "'")
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

    def expand(left, right):
        while left >= 0 and right < len(origin) and origin[left] == origin[right]:
            left -= 1
            right += 1

        return right - left - 1

    start = end = 0

    for i in range(len(origin)):
        length_1 = expand(i, i)
        length_2 = expand(i, i + 1)

        max_pal_length = max(length_1, length_2)
        if max_pal_length > end - start:
            start = i - (max_pal_length - 1) // 2
            end = i + max_pal_length // 2

    return origin[start:end + 1]

assert get_longest_palindrome("0123219") == "12321"
assert get_longest_palindrome("1012210") == "012210"


def are_parentheses_balanced(origin):
    
    stack = []
    if origin.count("(") == origin.count(")") and origin.count("{") == origin.count("}") and origin.count("[") == origin.count("]") and origin.count("<") == origin.count(">"):
        for i in origin:
            if i in "({[<":
                stack.append(i)
            elif i in ")}]>":
                open_bracket = stack.pop()
                if open_bracket == "(" and i == ")":
                    continue
                elif open_bracket == "{" and i == "}":
                    continue
                elif open_bracket == "[" and i == "]":
                    continue
    else: return False
    if stack: return False
    else: return True

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
