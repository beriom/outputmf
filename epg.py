import requests


url = 'http://m3u4u.com/xml/5g28nepzw9sk2kjyzpe9'


r = requests.get(url, stream=True, headers={'User-agent': 'Mozilla/5.0'})

with open(r'C:\Users\macelgomesfilho\Desktop\EPG\output/brasil_2.xml', 'wb') as f:
    f.write(r.content)