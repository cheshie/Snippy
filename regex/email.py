import re

nr_of_lines = int(input())
found = []

for x in [input() for x in range(nr_of_lines)]:
    found += re.findall(r"\b[a-zA-Z0-9_]+\b@\b\w+\b.\b\w+\b", x)
    
print(';'.join(sorted(list(set(found)))))

