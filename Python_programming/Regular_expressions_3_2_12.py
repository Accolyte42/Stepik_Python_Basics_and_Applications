import sys, re

pattern = r'\b[Aa]+\b'
#
# string = 'I need to understand the human mind'
# print(re.sub(pattern, 'computer', string))
# counter = 0
for line in sys.stdin:
    line = line.strip()
    if re.sub(pattern, 'argh', line) is not None:
        print(re.sub(pattern, 'argh', line, count=1))



