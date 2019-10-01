import requests
import sys

headers = {'User-Agent': 'Mozilla/12.0',
}
list = open(sys.argv[2], 'r')
for url in list:
    target = sys.argv[1]
    sendHTTPS = requests.get(target + str(url), timeout=10, headers=headers)
    requestHTTPS = sendHTTPS.status_code
    headHTTPS = sendHTTPS.headers
    print (str(requestHTTPS) + "<------>" + target + str(url) + str(headHTTPS))
