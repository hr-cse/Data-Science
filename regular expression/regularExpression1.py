import re

line = "we love bangladesh very much."

matchobj = re.match(r'(.*) bangladesh (.?) .*', line, re.M | re.I)

