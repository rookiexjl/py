# coding:utf-8

from fabric.api import *

env.user = 'root'
env.hosts = ['192.168.3.40', '192.168.3.41']
env.password = 'root1234'


@runs_once  # 查看本地系统信息，当多台主机时只运行一次
def local_task():
    local('uname -a')

def remote_task():
    with cd('/root'):
	run('ls -l')



