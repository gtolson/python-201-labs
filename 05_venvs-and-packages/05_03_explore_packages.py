#Do an online search for interesting Python packages on PyPI.
#You can search for something you're interested to do with your programming
#skills and add "Python package" to the search query.
#- What do you find?
#- Create a new virtual environment and install the package.
#- Check out its documentation and their "Getting Started" guide
#  and code examples, if there are any.
#- Can you get some basic functionality of the package to work locally?



import requests
import json

url = "http://ifconfig.io/all.json"
headers = {"Accept" :"application/json"}

payload = requests.get(url=url, headers=headers)

json_response = json.loads(payload.text)

print(json.dumps(json_response, indent=2))
