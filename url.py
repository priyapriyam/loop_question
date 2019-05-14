import requests
import json
import os
url = ("https://www.google.com/search?q=what+is+function&oq=what+is+&aqs=chrome.0.69i59j69i60j69i65j69i57j69i59j69i61.7893j0j7")
var = requests.get(url)
print var.content