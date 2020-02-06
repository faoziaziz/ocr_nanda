import requests

files = {'file': open('/home/faoziaziz/ocr_nanda/image/320220.png', 'rb')}

response = requests.post('https://api.ocr.proclubstudio.com/file', files=files)
print(response.json())
