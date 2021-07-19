import collections
import time

def times(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        dt = time.time() - st
        print(f'Time of work: {dt} sec')
        return res
    return wrapper

@times
def scramble1(s1, s2):
    for k, v in collections.Counter(s2).items():
        if s1.count(k) < v:
            return False
    return True

@times
def scramble2(s1, s2):
    for s in set(s2):
        if s1.count(s) < s2.count(s):
            return False
    return True

print(scramble1('jvaascptripytgsgbkdfnj', 'javascrpintpython'))
print(scramble2('jvaascptripytgsgbkdfnj', 'javascrpintpython'))