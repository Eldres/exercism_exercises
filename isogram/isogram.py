import re

def is_isogram(string):
    s = re.sub(r'[^a-zA-Z]', "", string).lower()  # replace regex pattern with empty space, using string
    occur_once = lambda letter: s.count(letter) == 1  # stores 'letter', which returns the count of the string once it reaches 1
    return all(map(occur_once, s))  # returns true when occur_once and s return true
