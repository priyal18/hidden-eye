#!/usr/bin/env python3
import argparse
import validators
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup,Comment

def basics(url):
	config={'forms':True,'comments':True,'passwords':True}
	report=""
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
					report=""+"Form Issue \n Insecure form action "+form.get('action')+" found in document!\n"

		if(config['comments']):
			for comment in comments:
				if(comment.find('key:')>-1):
					report+="Comment Issue \n key is found in the HTML comments,please remove it!\n"
	
		if(config['passwords']):
			for password in password_type:
				if(password.get('type')!='password'):
					report+="Input Issue \n Plain text Password input found, Please change Password type input!\n"

		#XSS vulnerability check
		report=xss_check(url,report)
	
	else:	
		fail="Invalid Url found!\n"
		return fail
	if report == "":
  		report="Sit back and Use this URL without any worry, as the URL is secure :)\n"

	
	return report

def xss_check(url,report):
	#with open('/media/slappy/7BF04F772FFAA9A0/raja/XSS-Freak/xss-payload-list.txt','r') as f:
	with open('realsecurity/xss-payload-list.txt','r') as f:
		for line in f:
			payload=line
			req = requests.post(url + payload)
			if payload in req.text:
				report+="XSS Vulnerablity Discovered! \n"
				report+="Refer to XSS payloads for further escalation"
				return report
	#report+="Secure from XSS Vulnerablity"
	return report