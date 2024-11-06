import re,json

pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(\d{1,2}\/\w{1,3}\/\d{1,4}):(\d{1,2}:\d{1,2}:\d{1,2}) \+\d{1,4}\] \"(GET|POST|PUT|DELETE|PATCH|HEAD|OPTIONS) (.*)\?(.*) HTTP\/\d.\d\" (\d{3,3})'

with open('apache_logs.txt','r') as lines:
    jsonExtract = []
    for line in lines:
        values = re.finditer(pattern,line)
        for match in values:
           jsonData = {"IP":match.group(1),"Date":match.group(2),"Time":match.group(3),",Method":match.group(4),"Path":match.group(5),"Parameter":match.group(6),"errorCode":match.group(7)}
           jsonExtract.append(jsonData)
        print(json.dumps(jsonExtract,indent=4))


        #https://regex101.com/r/VKccht/1
        #https://raw.githubusercontent.com/elastic/examples/refs/heads/master/Common%20Data%20Formats/apache_logs/apache_logs