# coding:utf-8
# 生产环境代码包发布管理

from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user = 'root'
env.hosts = ['192.168.2.193', '192.168.2.194']
env.passwords = 'root1234'

env.project_dev_source = '/data/dev/Lwebadmin'
env.project_tar_source = '/data/dev/releases'
env.project_pack_name = 'release'

env.deploy_project_root = '/data/www/Lwebadmin'
env.deploy_release_dir = 'releases'
env.deploy_current_dir = 'current'
env.deploy_version = time.strftime('%Y%m%d')+'v2'


@runs_once
def input_versionid():  # 获取用户输入的版本号，以便做版本回滚操作
    return prompt('please input project rollback version ID:', default='')


@task
def tar_source():  # 打包本地项目主目录，并将压缩包存储到本地压缩包目录
    print yellow('Start put package...')
    with lcd(env.project_dev_source):
	local('tar -czf %s.tar.gz') % (env.project_tar_source + env.project_pack_name)
    print green('Creating source package success!')


@task
def put_package():  # 上传任务函数
    print yellow('Start put package...')
    with settings(warn_only=True):
    	# 本地local命令需要配置capture=True才能捕获返回值
	with cd(env.deploy_project_root+env.deploy_release_dir):
	    run('mkidr %s' % (env.deploy_version))
    env.deploy_full_path = env.deploy_project_root + env.deploy_release_dir +
'/' + env.deploy_version
    with settings(warn_only=True):
        result = put(env.project_tar_source + env.project_pack_name +'.tar.gz',
env.deploy_full_path)
    if result.failed and not confirm('put file failed, Continue[Y/N]?'):
        abort('Aborting file put task!')

    with cd(env.deploy_full_path):
	run('tar -zxvf %s.tar.gz' % (env.project_pack_name)
        run('rm -rf %s.tar.gz' % (env.project_pack_name)

    print green('Put & untar package success!')


@task
def make_symlink():  # 为当前版本目录做软连接
    print yellow('update current symlink...')
    env.deploy_full_path = env.deploy_project_root + env.deploy_release_dir +
'/' + env.deploy_version
    with settings(warn_only=True):
        run('rm -rf %s') % (env.deploy_project_root + env.deploy_current_dir)
        run('ln -s %s %s' % (env.deploy_full_path + env.deploy_project_root +
env.deploy_current_dir))
    print green('Project version ID error,abort!')


@task
def rollback():  # 版本回滚任务函数
    print yellow('rollback project version')
    versionid = input_versionid()
    if versionid=='':
        abort('Project version IS error,abore!')
    env.deploy_full_path = env.deploy_project_root + env.deploy_release_dir +
'/' + versionid
    run('rm -rf %s') % (env.deploy_project_root + env.deploy_current_dir)
    run('ln -s %s %s' % (env.deploy_full_path + env.deploy_project_root +
env.deploy_current_dir))
    print green('rollback success!')


@task
def go:
    tar_source()
    put_package()
    make_symlink()


  
    print green('Project version ID error,abort!')






	




