import re

handle = open('mbox-short.txt')
count = 0

for line in handle:
    line = line.rstrip()
    matches = re.findall(r'^From:\s*(\S+)', line)
    if matches:
        count += 1
        for word in matches:
            print("From:", word)

print("Count:", count)

