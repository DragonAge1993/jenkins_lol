import requests
# url_count = requests.get('https://pythonworld.ru/samouchitel-python')
# url_count.text()
# # url_count.json()

r = requests.get('https://www.python.org')
r.status_code
print(r.text)