import os

class Config():
	#in shell type: export TELTOKEN=past_you_bot_token_here
	TELPASS = os.environ.get('TELPASS')
	PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080', 'urllib3_proxy_kwargs': {'username': 'learn', 'password': TELPASS}}
	TOKEN = os.environ.get('TELTOKEN')
	


    
