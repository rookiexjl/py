# coding:utf-8
# 实现集中式的病毒扫描

import time
import pyclamd
from threading import Thread

class Scan(Thread):
    def __init__(self, IP, scan_type, file):
	"""构建方法，参数初始化"""
	Thread.__init__(self)
	self.IP = IP
	self.scan_type = scan_type
	self.file = file
	self.connstr = ""
	self.scanresult = ""


    def run(self):
	try:
            cd = pyclamd.ClamdNetworkSocket(self.IP, 22)  # 创建忘了套接字连接对象
	    if cd.ping():  # 探测连通性
	        self.connstr = self.IP + " connection [OK]"
	        cd.reload()  # 重载clamd病毒特征库，建议更新病毒库后座reload()操作
	        if self.scan_type == "contscan_file":  # 选择不同的扫描模式
		    self.scanresult="{0}\n".format(cd.contscan_file(self.file))
	        elif self.scan_type == "multiscan_file":
		    self.scanresult="{0}\n".format(cd.multiscan_file(self.file))
	        elif self.scan_type == "scan_file":
		    self.scanresult="{0}\n".format(cd.scan_file(self.file))
	        time.sleep(1)  # 线程挂起1秒
	    else:
	        self.connstr = self.IP + " ping error.exit"
	        return
	except Exception,e:
	    self.constr = self.IP + " " + str(e)


IPs = ('192.168.2.193', '192.168.2.194')
scantype = "multiscan_file"
scanfile = '/data/'  # 扫描指定路径
i = 1

threadnum = 2
scanlist = []

for ip in IPs:
    currp = Scan(ip, scantype, scanfile)
    scanlist.append(currp)

    if i%threadnum==0 or i==len(IPs):
	for task in scanlist:
	    task.start()

	for task in scanlist:
	    task.join()
	    print task.connstr
	    print task.scanresult
	scanlist = []
    i+=1

print 'success'

   
	
