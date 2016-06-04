import requests
import requests.packages.urllib3
import requests.packages.urllib3.contrib.pyopenssl
import requests.packages.urllib3.connection
import requests.packages.urllib3.util

import urllib3
import urllib3.contrib.pyopenssl

print('requests', requests.__version__)
print('requests urllib3', requests.packages.urllib3.__version__)
print('urllib3', urllib3.__version__)

print('requests urllib3 is urllib3', urllib3 is requests.packages.urllib3)

print(requests.packages.urllib3, urllib3)

print(requests.packages.urllib3.connection.ssl_wrap_socket, requests.packages.urllib3.contrib.pyopenssl.ssl_wrap_socket)

print(requests.packages.urllib3.util.HAS_SNI)
print(requests.packages.urllib3.util.IS_PYOPENSSL)

print('no inject:')

requests.get('https://www.wikipedia.org/')
requests.get('https://testssl-expire-r2i2.disig.sk/index.en.html', verify=False)

try:
    urllib3.contrib.pyopenssl.inject_into_urllib3()
except Exception as e:
    print(e)

print('urllib3 inject:')

print('requests urllib3 is urllib3', urllib3 is requests.packages.urllib3)

print(requests.packages.urllib3, urllib3)
print(requests.packages.urllib3.connection.ssl_wrap_socket, requests.packages.urllib3.contrib.pyopenssl.ssl_wrap_socket)

print(requests.packages.urllib3.util.HAS_SNI)
print(requests.packages.urllib3.util.IS_PYOPENSSL)

requests.get('https://www.wikipedia.org/')
requests.get('https://testssl-expire-r2i2.disig.sk/index.en.html', verify=False)

try:
    requests.packages.urllib3.contrib.pyopenssl.inject_into_urllib3()
except Exception as e:
    print(e)

print('requests inject:')

print('requests urllib3 is urllib3', urllib3 is requests.packages.urllib3)

print(requests.packages.urllib3, urllib3)
print(requests.packages.urllib3.connection.ssl_wrap_socket, requests.packages.urllib3.contrib.pyopenssl.ssl_wrap_socket)

print(requests.packages.urllib3.util.HAS_SNI)
print(requests.packages.urllib3.util.IS_PYOPENSSL)

requests.get('https://www.wikipedia.org/')
requests.get('https://testssl-expire-r2i2.disig.sk/index.en.html', verify=False)
