# coding:utf-8
# 文件打包、上传与校验

from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user = 'root'
env.hosts = ['192.168.2.194', '192.168.2.193']
env.passwords = 'root1234'


@runs_once
def tar_task():
    with cd('/data/logs'):
        local('tar -czf access.tar.gz access.log')


@task
def put_task():
    run('mkdir -p /data/logs')
    with cd('/data/logs'):
        with settings(warn_only=True):
            result = put('/data/logs/access.tar.gz', '/data/logs/access.tar.gz')
            if result.failed and not confirm('put file failed, Continue[Y/N]?'):
                abort('Aborting file put task!')


@task
def check_task():
    with settings(warn_only=True):
        lmd5 = local('md5sum /data/logs/access.tar.gz', capture=True).split(' ')[0]
        rmd5 = run('md5sum /data/logs/access.tar.gz').split(' ')[0]
    if lmd5==rmd5:
	print 'OK'
    else:
	print 'ERROR'

