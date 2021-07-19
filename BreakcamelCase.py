def solution(s: str) -> str:
    end_list = [' ' + letter if letter.isupper() else letter for letter in list(s) ]
    return ''.join(end_list)