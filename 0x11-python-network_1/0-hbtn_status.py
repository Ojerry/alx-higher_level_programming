#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        response = response.read()
        print("Body response:",end="$\n")
        print("\t- type: {}".format(type(response)), end="$\n")
        print("\t- content: {}".format(response), end="$\n")
        print("\t- utf8 content: {}".format(response.decode(encoding='utf-8')), end="$\n")
