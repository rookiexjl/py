# coding:utf-8
# 实现堡垒机模式下的远程文件上传

import paramiko
import os,sys,time

blip = '192.168.2.194'
bluser = 'root'
blpasswd = 'root1234'

hostname = '192.168.2.193'
userhost = 'root'
password = 'root1234'

tmpdir = '/tmp'
remotedir = '/data'
localpath = '/home/nginx_access.tar.gz'
tmppath = tmpdir+'/nginx_access.tar.gz'
remotepath = remotedir + '/nginx_access_hd.tar.gz'
port = 22
passinfo = '\'s password: '
paramiko.util.log_to_file('syslogin.log')

t = paramiko.Transport((blip,port))
t.connect(username=bluser, password=blpasswd)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put(localpath, tmppath)
sftp.close()

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=blip, username=bluser, password=blpasswd)

channel = ssh.invoke_shell()
channel.settimeout(10)

buff = ''
resp = ''
channel.send('ssh '+userhost+'@'+hostname+':'+remotepath+'\n')
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

print buff
channel.close()
ssh.close()
                    
