import urllib.request, json

with urllib.request.urlopen("file:///C:/Users/jsand/Documents/Snow/Development/Python/LEAP%20Motion%20Wrapper/JSONViewer.html") as url:
    data = json.loads(url.read().decode())
    print(data)
