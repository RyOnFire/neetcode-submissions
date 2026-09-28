from typing import List

def read_integers() -> List[int]:
    inp = input()
    read = [int(x) for x in inp.split(",")]
    return read

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())