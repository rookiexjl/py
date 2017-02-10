# codng:utf-8

from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.usr = 'root'
env.gateway = '192.168.2.193'
env.hosts = ['192.168.2.194']
env.passwords = {
    'root@192.168.2.193:22': 'root1234'
    'root@192.168.2.194:22': 'root1234'
   }

lpackpath = '/home/install/lnmp0,9.tar.gz'
rpackpath = '/tmp/install'


@task
def put_task():
    run('mkdir -p /tmp/install')
    with settings(warn_only=True):
        result = put(lpackpath, rpackpath) 
    if result.failed and not confirm('put file failed, Continue[Y/N]?'):
        abort('Aborting file put task!')

@task
def run_task():
    with cd('/tmp/install'):
        run('tar -zxvf Inmp0.9.tar.gz')
        with cd('lnmp0.9/'):
            run('./centos.sh')


@task
def go():
    put_task()
    run_task()



