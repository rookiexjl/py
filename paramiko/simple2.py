# coding:utf-8

import paramiko
 
socks=('127.0.0.1',22)
testssh=paramiko.Transport(socks)
testssh.connect(username='root',password='root1234')
print 'sucess'
sftptest=paramiko.SFTPClient.from_transport(testssh)
#remotepath="/tmp/a.log"
#localpath="/tmp/c.log"
#sftptest.put(remotepath,localpath)
#sftptest.close()
sftptest.put('/home/user/info.db', '/data/user/info.db')  # 上传文件
sftptest.get('/data/user/info_1.db', '/home/usrt/info_1.db')  #下载文件
sftptest.mkdir('/home/userdir',0755)  # 创建目录
sftptest.rmdir('/home/userdir')  # 删除目录
sftptest.rename('/home/user.sh','/home/test/sh')  # 文件重命名
print sftptest.stat('/home/test.sh')  # 打印文件信息
print sftptest.listdir('/home')  # 打印目录列表

testssh.close()
