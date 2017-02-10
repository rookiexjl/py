# coding:utf-8
# 实现堡垒机模式下的远程命令执行

import  paramiko
import os,sys,time

blip = '192.168.2.194'
bluser = 'root'
blpasswd = 'root1234'

hostname = '192.168.2.193'
userhost = 'root'
password = 'root1234'

port = 22
passinfo = '\'s password: '
paramiko.util.log_to_file('syslogin.log')

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=blip, username=bluser, password=blpasswd)

channel = ssh.invoke_shell()
channel.settimeout(10)

buff = ''
resp = ''
channel.send('ssh '+userhost+'@'+hostname+'\n')
while not buff.endswith(passinfo):
    try:
	resp = channel.recv(9999)
        print resp
    except Exception,e:
        print 'Error info:%s connection time.' % (str(e))
	channel.close()
	ssh.close()
	sys.exit()
    buff += resp
    if not buff.find('yes/no')==-1:
	channel.send('yes\n')
	buff = ''

channel.send(password+'\n')

buff = ''
while not buff.endswith('# '):
    resp = channel.recv(9999)
    print resp
    if not resp.find(passinfo)==-1:
	print 'Error info: Authentication failed.'
	channel.close()
	ssh.close()
	sys.exit()
    buff += resp

channel.send('ifconfig\n')
buff = ''
try:
    while buff.find('# ')==-1:
	resp = channel.recv(9999)
	buff += resp
except Exception, e:
    print 'error info:'+str(e)

print buff
channel.close()
ssh.close()



 

