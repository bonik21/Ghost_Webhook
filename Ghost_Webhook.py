# abcd.com/webhookreq에 요청 들어온 그대로 콘솔에 출력
import os, sys
import configparser
import requests
import socket
from flask import Flask, request, jsonify

app = Flask(__name__)


#info
Ghost_Webhook_version = 1.0
Ghost_Webhook_path = os.path.dirname(os.path.realpath(__file__))


# 내부 아이피 확인 
# ini파일에서 정보 불러오기
config = configparser.ConfigParser()
config.read(f'{Ghost_Webhook_path}/Ghost_Webhook.ini', encoding='UTF8')
settings = config['SETTINGS']
IP_AUTO_DETECT = settings["IP_AUTO_DETECT"] 
if IP_AUTO_DETECT == 'Y':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('192.255.255.255', 1))
    HOST_IP = s.getsockname()[0]
    s.close()

    # ini파일에 내부 아이피 작성
    config = configparser.ConfigParser()
    config.optionxform = str
    config.read(f'{Ghost_Webhook_path}/Ghost_Webhook.ini', encoding='UTF8')
    with open(f'{Ghost_Webhook_path}/Ghost_Webhook.ini', "w", encoding='UTF8') as f:
        config.set('SETTINGS', "GHOST_WEBHOOK_IP", f"{HOST_IP}")    
        config.write(f)


# ini파일에서 정보 불러오기
config = configparser.ConfigParser()
config.read(f'{Ghost_Webhook_path}/Ghost_Webhook.ini', encoding='UTF8')
settings = config['SETTINGS']
IP_AUTO_DETECT = settings["IP_AUTO_DETECT"] 
GHOST_WEBHOOK_IP = settings["GHOST_WEBHOOK_IP"]
GHOST_WEBHOOK_PORT = settings["GHOST_WEBHOOK_PORT"]
TELEGRAM = settings["TELEGRAM"]
TELEGRAM_TOKEN = settings["TELEGRAM_TOKEN"]
CHAT_ID = settings["CHAT_ID"]
DISCORD = settings["DISCORD"]
WEBHOOKURL = settings["WEBHOOKURL"]
USERNAME = settings["USERNAME"]
AVATAR_URL = settings["AVATAR_URL"]


# 텔래그램 전송
def send_telegram(message):    
    if TELEGRAM == 'Y':
        base_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": message}
        result = requests.post(base_url, data=data)
        return result.status_code
    else:
        return


# 디스코드 전송
def send_discord(message):
    if DISCORD == 'Y':
        data = {
    "content": message,
    "username": USERNAME,
    "avatar_url": AVATAR_URL,
    }
        result = requests.post(WEBHOOKURL, json=data)
        return result.status_code
    else:
        return


# Ghost의 Post Published 웹훅
@app.route('/post_published', methods=['POST'])
def post_published():
    if request.method == 'POST':
        try:
            data = request.get_json()  # JSON 데이터를 딕셔너리로 변환
            post_url = data["post"]["current"]["url"]  # 받은 JSON 데이터를 딕셔너리로 출력            
            # 텔레그램, 디스코드 전송
            if not post_url == '':
                send_telegram(post_url)
                send_discord(post_url)
        except Exception as e:
            return e, 400
    return ""


# Ghost의 Post Updated 웹훅
@app.route('/post_updated', methods=['POST'])
def post_updated():
    if request.method == 'POST':
        try:
            data = request.get_json()  # JSON 데이터를 딕셔너리로 변환
            post_url = data["post"]["current"]["url"]  # 받은 JSON 데이터를 딕셔너리로 출력            
            # 텔레그램, 디스코드 전송
            if not post_url == '':
                send_telegram(post_url)
                send_discord(post_url)            
        except Exception as e:
            return e, 400
    return ""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=GHOST_WEBHOOK_PORT, debug=True, threaded=True)