import sys, re

pattern = r'\b(\w)(\w)([\w]*)\b'
#
# string = 'this !is. ?n1ce,'
# print(re.sub(pattern, r'\2\1\3', string))

# counter = 0
for line in sys.stdin:
    line = line.strip()
    if re.sub(pattern, 'argh', line) is not None:
        print(re.sub(pattern, r'\2\1\3', line))



