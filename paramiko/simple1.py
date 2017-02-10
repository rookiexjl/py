# coding:utf-8
# 实现远程SSH命令

import paramiko

#host1 = '192.168.2.194'
username = 'root'
password = 'root1234'
paramiko.util.log_to_file('syslogin.log')

ssh = paramiko.SSHClient()

ssh.load_system_host_keys()
#ssh.connect('127.0.0.1', username=username, password=password)
#known_host="/root/.ssh/known_hosts" # 前提，这里应该存在与127.0.0.1有关的信息。
#ssh.load_system_host_keys(known_host)
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('127.0.0.1', username=username, password=password,port=22)
#ci = paramiko.SSHClient()
# = paramiko.SSHClient()
#ssh.connect(hostname=host1,username=user1, password=pass1)
stdin,stdout,stderr = ssh.exec_command('free -m')
print stdout.read()
ssh.close()


