import requests
import re

page = requests.get("https://www.columbia.edu/~fdc/sample.html").text
a = re.findall("<h3.*>.*<\/h3>", page)

first_filter=[]
for i in a:
    filtered = re.sub("<h3.*\">", '', i);
    first_filter.append(filtered)

result = []

for i in first_filter:
    filtered = re.sub("</h3.*>", '', i);
    result.append(filtered )

print(result)