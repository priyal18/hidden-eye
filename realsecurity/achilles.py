#!/usr/bin/env python3
import argparse
import validators
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup,Comment

def basics(url):
	config={'forms':True,'comments':True,'passwords':True}
	report=""
	description=""
	fail=""
	if validators.url(url):
		result_html=requests.get(url).text
		parsed_html=BeautifulSoup(result_html,"html.parser")
		forms=(parsed_html.find_all("form"))
		comments=parsed_html.find_all(string=lambda test:isinstance(test,Comment))
		password_type=parsed_html.find_all('input',{'name':'password'})

		if(config['forms']):
			for form in forms:
				if((form.get('action').find("https")<0) and (urlparse(url).scheme!='https')):
					report=""+"Form Issue \n"
					description+="Insecure form action "+form.get('action')+" found in document!\n"

		if(config['comments']):
			for comment in comments:
				if(comment.find('key:')>-1):
					report+="Comment Issue \n"
					description+="key is found in the HTML comments,please remove it!\n"
	
		if(config['passwords']):
			for password in password_type:
				if(password.get('type')!='password'):
					report+="Input Issue \n"
					description+="Plain text Password input found, Please change Password type input!\n"

		#XSS vulnerability check
		report,description=xss_check(url,report,description)
	
	else:	
		fail="Invalid Url found!"
		return fail,description
	if report == "":
  		report="Nice job! Your HTML document is secure!"

	
	return report,description

def xss_check(url,report,description):
	#with open('/media/slappy/7BF04F772FFAA9A0/raja/XSS-Freak/xss-payload-list.txt','r') as f:
	with open('realsecurity/xss-payload-list.txt','r') as f:
		for line in f:
			payload=line
			req = requests.post(url + payload)
			if payload in req.text:
				report+="XSS Vulnerablity Discovered!\n"
				description+="Refer to XSS payloads for further escalation\n"
				return report,description
	#report+="Secure from XSS Vulnerablity"
	return report,description