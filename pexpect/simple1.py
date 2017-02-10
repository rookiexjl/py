# coding:utf-8
# pxssh

import pexpect.pxssh
import getpass

try:
    s = pexpect.pxssh.pxssh()
    hostname = raw_input('hostname: ')
    username = raw_input('username: ')
    password = getpass.getpass('please input password: ')
    s.login(hostname, username, password)
    s.sendline('uptime')
    s.prompt()
    print s.before
    s.sendline('ls -l')
    s.prompt()
    print s.before
    s.sendline('df')
    s.prompt()
    print s.before
    s.logout()
except pexpect.pxssh.ExceptionPxssh, e:
    print 'pxssh failed on login.'
    print str(e)

