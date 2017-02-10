# coding:utf-8

from fabric.api import *

env.user = 'root'
env.hosts = ['192.168.2.193, 192.168.2.194']
env.password = 'root1234'


@runs_once
def input_raw():
    return prompt('please input directory name:', default='/home')


def worktask(dirname):
    run('ls -l '+dirname)


@task
def go():
    getdirname = input_raw()
    worktask(getdirname)

