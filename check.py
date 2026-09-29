import os, json, urllib.request, urllib.parse

CURRENT = os.environ["CURRENT_VERSION"]
url = "https://itunes.apple.com/lookup?id=1359706682&country=iq"
data = json.load(urllib.request.urlopen(url))
version = data["results"][0]["version"]
print("Version:", version)

if version != CURRENT:
    api = f"https://api.telegram.org/bot{os.environ['BOT_TOKEN']}/sendMessage"
    body = urllib.parse.urlencode({
        "chat_id": os.environ["CHAT_ID"],
        "text": f"Standoff 2 update is out! New version: {version}",
    }).encode()
    urllib.request.urlopen(api, data=body)
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write("updated=true\n")
