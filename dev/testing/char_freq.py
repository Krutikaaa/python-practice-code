''' Given a string, count the frequency of each character.
'''
from collections import Counter

char = 'jqhdjqhd'
def char_frequency():
    freq = dict(Counter(char))
    print(freq)
    return freq

def char_freq():
    freq = {}
    for c in char:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    print(freq)
    return freq



obj = char_frequency()
obj = char_freq()