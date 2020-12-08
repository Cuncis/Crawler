import requests
import re
import urllib.parse as urlparse


# links + directories
target_url = "http://bukalapak.com/"
pattern = '(?<=href=").*?(?=")'
target_links = []


def extract_links_from(url):
    response = requests.get(url)
    return re.findall(pattern, str(response.content))


def crawl(url):
    href_links = extract_links_from(url)
    for links in href_links:
        link = urlparse.urljoin(url, links)

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)


crawl(target_url)
