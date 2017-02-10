# coding:utf-5
# 部署LNMP业务环境

from fabric.colors import *
from fabric.api import *

env.user = 'root'
env.roledefs = {  # 定义业务角色分组
    'webservers':['192.168.2.193','192.168.2.194']
    'dbservers': ['192.168.3.39']
}
env.passwords = {
    'root@192.168.2.193:22': 'root1234',
    'root@192.168.2.194:22': 'root1234',
    'root@192.168.3.39:22': 'root1234'
}

@roles('webservers')
def webtask():
    print yellow('Install nginx php php-fpm...')
    with settings(warn_only=True):
	run('yum -y install nginx')
	run('yum -y install php-fpm php-mysql php-mbstring php-xml php-mcrypt php-gd')
        run('chkcofig --levels 235 php-fpm on')
        run('chkcofig --levels 235 nginx on')


@roles('dbservers')
def datask():
    print yellow('Install Mysql...')
    with settings(warn_only=True):
        run('yum -y install mysql mysql-server')
        run('chkcofig --levels 235 mysqld on')


@roles('webservers', 'dbservers')
def publictask():
    print yellow('Install epel ntp...')
    with settings(warn_only=True):
        rum('rpm -Uvh http:/www....rpm')
        run('yum -y install ntp')


def deploy():
    execute(publictask)
    execute(webtask)
    execute(dbtask)


