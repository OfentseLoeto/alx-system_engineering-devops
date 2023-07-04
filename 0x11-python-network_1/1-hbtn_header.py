#!/usr/bin/python3
# Module to send a request to a URL and display the value of the X-Request-Id variable.
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        header = response.getheader('X-Request-Id')

        print(header)
