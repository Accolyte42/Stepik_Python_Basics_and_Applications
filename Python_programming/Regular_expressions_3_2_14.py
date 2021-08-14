# put your python code here

import sys, re

pattern = r'((\w*)?(\w){2,})?'
#
# string = 'this !is. ?n1ce,'
# print(re.sub(pattern, r'\2\1\3', string))

# counter = 0
for line in sys.stdin:
    line = line.strip()
    if re.match(pattern, line) is not None:
        print(re.sub(pattern, r'\1', line))
        print(re.sub(pattern, r'\2', line))
        print(re.sub(pattern, r'\3', line))
        # print(re.sub(pattern, r'\3', line))
        # print(re.sub(pattern, r'\4', line))
        # print(re.sub(pattern, r'\1\2\3', line))


