import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "google.com"
with open("/home/cuncis/Downloads/subdomains.txt", "r") as word_list:
    for line in word_list:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print("[+] Discovered subdomain -> " + test_url)
        else:
            print(test_url + " Failed to Discover subdomain")
