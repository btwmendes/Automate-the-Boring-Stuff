import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
print(res.status_code) #200 means success. 404 is bad

print(len(res.text))
print(res.text[:500])

res.raise_for_status() #works for try/except statement
badRes = requests.get("https://arukljamtek")
print(badRes.raise_for_status())