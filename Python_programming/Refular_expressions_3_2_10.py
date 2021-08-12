import sys, re

pattern = r'\b(\w+)\1\b'
#
# string = 'cattcatt catcc tagtag cattagtag'
# print(re.search(pattern, string))
# counter = 0
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line) is not None:
        print(line)




