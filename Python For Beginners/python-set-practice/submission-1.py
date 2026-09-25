from typing import List

def contains_duplicate(words: List[str]) -> bool:
    length = len(words)
    my_tuple = set(words)
    my_list = list(my_tuple)
    if len(my_list) < length:
        return True
    else:
        return False




# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
