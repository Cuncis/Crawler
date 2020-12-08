import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "192.168.1.107/DVWA/"
with open("/home/cuncis/Downloads/files-and-dirs-wordlist.txt", "r") as word_list:
    for line in word_list:
        word = line.strip()
        test_url = target_url + word
        response = request(test_url)
        if response:
            print("[+] Discovered subdomain -> " + test_url)
