import requests, re

url_A = input()
url_B = input()

res_A = requests.get(url_A)

pattern = url_B