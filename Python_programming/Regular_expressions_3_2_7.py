import sys, re

pattern = 'cat'
#
# string = 'catcatccgcat'
# print(len(re.findall(pattern, string)))
counter = 0
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(pattern, line)) > 1:
        print(line)