import logging
import json
# import datetime

from fabric.api import *  # NOQA
from fabric.contrib.files import * # NOQA

env.user = 'root'

logger = logging.getLogger('fabric')

def test():
    print 'we are testing'


def load():
    '''
    Load servers info
    '''

    server_data = open('servers.json')
    env.servers = json.load(server_data)

    server_data.close()

    print 'Load servers done! %s' % env.servers

def staging():
    load_server('staging_dashboard')

def production():
    load_server('production_dashboard')

def load_server(server):
    server_data = env.servers[server]

    print 'Using %s' % server

    # load server to global
    env.server = server_data
    env.hosts = [server_data['ip']]

def deploy():
    if env.server['name'] == 'staging':
        logger.info('Deploy staging')
        deploy_staging()
    elif env.server['name'] == 'production':
        logger.info('Deploy staging')
        deploy_master()

def deploy_staging():
    with cd('/root/src/bryony/'):
        run('git checkout develop')
        run('git pull')
        with cd('/root/src/bryony/deploy/'):
            run('sh frontend.sh')
            run('sh restart-dashboard.sh')

def deploy_master():
    with cd('/root/src/bryony/'):
        run('git checkout master')
        run('git pull')
        with cd('/root/src/bryony/deploy/'):
            run('sh frontend.sh')
            run('sh restart-dashboard.sh')
