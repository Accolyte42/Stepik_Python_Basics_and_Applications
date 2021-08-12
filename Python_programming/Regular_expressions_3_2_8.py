import sys, re

pattern = r'z.{3}z'
#
# string = 'cat2 catcc gcat cat'
# print(re.search(pattern, string))
# counter = 0
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line) is not None:
        print(line)