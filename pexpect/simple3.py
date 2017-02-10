# coding: utf-8
# 远程文件自动打包并下载
import pexpect
import sys

ip = '192.168.2.193'
user = 'root'
password = 'root1234'
target_file = '/data/logs/nginx_access.log'

child = pexpect.spawn('/usr/bin/ssh', [user+'@'+ip])
fout = file('mylog.txt', 'w')
child.logfile = fout

try:
    child.expect('(?i)password')
    child.sendline(password)
    child.expect('#')
    child.sendline('tar -czf /data/nginx_access.tar.gz '+target_file)

    child.expect('#')
    print child.before
    child.sendline('exit')
    fout.close()
except EOF:
    print 'expect EOF'
except TIMEOUT:
    print 'expect TIMROUT'


child = pexpect.spawn('/usr/bin/scp', [user+'@'+ip+':/data/nginx_access.tar.\
gz','/home'])
fout = file('mylog.txt','a')
child.logfile = fout
try:
    child.expect('(?i)password')
    child.sendline(password)
    child.expect(pexpect.EOF)
except EOF:
    print 'expect EOF'
except TIMEOUT:
    print 'expect TIMEOUT'

