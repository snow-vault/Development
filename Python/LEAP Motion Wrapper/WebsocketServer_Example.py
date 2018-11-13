import urllib.request
import json
req = urllib.request.urlopen("http://localhost:6437")
opener = urllib.build_opener()
f = opener.open(req)
json = json.loads(f.read())
print (json)
