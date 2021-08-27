import re

nr_of_lines = int(input())
found = []

Regex_Pattern = r"\b[a-zA-Z0-9_]+\b@\b\w+\b.\b\w+\b"
for x in [input() for x in range(nr_of_lines)]:
    found += re.findall(Regex_Pattern, x)
    
print(';'.join(sorted(list(set(found)))))

