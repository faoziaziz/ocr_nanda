import requests

files = {'file': open('image/4803.png', 'rb')}

response = requests.post('https://api.ocr.proclubstudio.com/file', files=files)
print response
print(response.json()['result'])

print response

if response.status_code==200:
    print "hore"


