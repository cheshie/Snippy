
ex1 = [1, 2, 3, 4]
ex2 = [1, 2, 5, 5]

# Print two lists side by side
for i in range(len(ex1)):
    print(ex1[i], "{:>35}".format(ex2[i]))


# Another way 
"\n".join("{} {}".format(x, y) for x, y in zip(ex1, ex2))

from difflib import Differ
from pprint import pprint
from sys import stdout
sys.stdout.writelines(list(d.compare(ex1, ex2))

# TODO: Comparing with colors?
