from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/get-token')
def getToken():

    url = "https://merchant-api.ifood.com.br/authentication/v1.0/oauth/token"

    payload = "grantType=client_credentials&clientId=2bdea3b6-71db-49e1-bbee-fc44d3ecb992&clientSecret=s6bzwejfhujg4j2mpclmo3kuwlw268xvfk40njvtpjjvabs599njsx5twnyji1mdzhc45npcw0euogcl1jo06syipwfi3jb8au1"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

    return response.text