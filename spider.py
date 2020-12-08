import requests
import re


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


# links + directories
target_url = "bukalapak.com"

response = request(target_url)
pattern = '(?<=href=").*?(?=")'

# print(response.content)
href = re.findall(pattern, response.content.decode("utf-8"))

for links in href:
    print(links)
