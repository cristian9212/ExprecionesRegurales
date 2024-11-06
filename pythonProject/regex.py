import re

pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(\d{1,2}\/\w{1,3}\/\d{1,4})'

with open('apache_logs.txt','r') as lines:
    for line in lines:
        values = re.finditer(pattern,line)
        for match in values:
            print(match.group(1))
            print(match.group(2))