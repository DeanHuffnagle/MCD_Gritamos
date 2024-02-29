import os

import requests
import file_io as io
from dotenv import load_dotenv

load_dotenv()
PROXY_URL = os.getenv("PROXY_URL")
API_KEY = os.getenv("WEBSHARE_API_KEY")
PROXY_SERVER_FILE_PATH = "TextFiles/proxyServers.txt"

def getRandomProxyServer():
    proxy = requests.get(
        "https://ipv4.webshare.io/",
        proxies={
            "http": PROXY_URL,
            "https": PROXY_URL
        }
    )
    print(proxy)
    return proxy


def checkRepeats(numTimes):
    array = []
    tries = 0
    repeatCount = 0
    while len(array) < numTimes:
        proxy = getRandomProxyServer()
        if proxy not in array:
            array.append(proxy)
        else:
            repeatCount += 1
        tries += 1
    print(f"{numTimes} successful connections took {tries} tries.")
    return repeatCount


def getProxyList():
    print("starting request")
    array = []
    response = requests.get(
        "https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=10",
        headers={"Authorization": API_KEY}
    )
    print("finished request")
    JSON_object = response.json()
    for i in JSON_object["results"]:
        address = i["proxy_address"]
        port = i["port"]
        array.append(f'{address}:{port}')
    print("returning array")
    return array

def getToken():
    config_response = requests.get(
        "https://proxy.webshare.io/api/v2/proxy/config/",
        headers={"Authorization": API_KEY}
    )
    config_object = config_response.json()
    return config_object['proxy_list_download_token']

def dowloadProxyList(token):
    response = requests.get(
        f"https://proxy.webshare.io/api/v2/proxy/list/download/{token}/-/any/sourceip/backbone/-/"
    )
    io.copy_string_to_file(response.text, PROXY_SERVER_FILE_PATH)
    return


if __name__ == "__main__":
    token = getToken()
    dowloadProxyList(token)
