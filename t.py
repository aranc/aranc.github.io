import json

j = json.load(open("../bookmarks-2021-05-16.json"))

print("<html>")
print("<body>")
for _ in j['children'][1]['children'][3]['children']: 
    print(f" <\"{_['uri']}\">{_['title']}</a> ")                                                                                                     
print("</body>")
print("</html>")


