import collections

def mix(s1, s2):
    cs1 = collections.Counter([c for c in s1 if c.islower()])
    cs2 = collections.Counter([c for c in s2 if c.islower()])
    elements_one_str = {}
    elements_two_str = {}
    elements_equally = {}
    max_identity = 0
    end_str = []

    for char in sorted(set(list(cs1.keys()) + list(cs2.keys()))):
        s1_amount = cs1.get(char, 0)
        s2_amount = cs2.get(char, 0)
        if s1_amount > 1 or s2_amount > 1:
            if max(s1_amount, s2_amount) > max_identity:
                max_identity = max(s1_amount, s2_amount)
            if s1_amount > s2_amount:
                elements_one_str.update({char: s1_amount})
            elif s1_amount < s2_amount:
                elements_two_str.update({char: s2_amount})
            else:
                elements_equally.update({char: s1_amount})
    
    for i in range(max_identity, 1, -1):
        end_str.extend([
            '1:' + char * value 
            for char, value in elements_one_str.items() 
            if value == i
        ])
        end_str.extend([
            '2:' + char * value 
            for char, value in elements_two_str.items() 
            if value == i
        ])
        end_str.extend([
            '=:' + char * value 
            for char, value in elements_equally.items() 
            if value == i
        ])

    return '/'.join(end_str)
