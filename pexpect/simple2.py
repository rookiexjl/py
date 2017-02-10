# coding:utf-8
# 实现一个自动化FTP操作

from __future__ import unicode_literals
import pexpect
import sys

child = pexpect.spawnu('vsftpd 192.168.3.39')  # 运行ftp命令
child.expect('(?i)name .*: ')
child.sendline('root')
child.expect('(?i)password')
child.sendline('root1234')
child.expect('ftp> ')
child.sendline('bin')
child.expect('ftp> ')
child.sendline('get robots.txt')
child.expect('ftp> ')
sys.stdout.write(child.before)
print("Escape character is '^]'.\n")
sys.stdout.write(child.after)
sys.stdout.flush()
child.interact()
child.sendline('bye')
child.close()

