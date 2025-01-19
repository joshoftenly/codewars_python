def solution(string):
    reversed_str = ""
    length = len(string)
    for x in string:
        reversed_str += string[length - 1]
        length -= 1
    return reversed_str


solution("world")