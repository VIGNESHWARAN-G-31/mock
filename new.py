import requests
res = requests.get("https://huggingface.co")
print(res.status_code)
