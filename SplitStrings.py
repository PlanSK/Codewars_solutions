    # ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    # ("asdfads", ['as', 'df', 'ad', 's_']),
    # ("", []),
    # ("x", ["x_"]),

def solution(s: str) -> list:
    return [s[i:i+2] if len(s[i:i+2]) == 2 else s[i]+"_" for i in range(0, len(s), 2)]

s = ['asdfadsf', 'asdfads', '', 'x']

for element in s:
    print(solution(element))