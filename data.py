__author__ = 'Jan Bogaerts'
__copyright__ = "Copyright 2016, AllThingsTalk"
__credits__ = []
__maintainer__ = "Jan Bogaerts"
__email__ = "jb@allthingstalk.com"
__status__ = "Prototype"  # "Development", or "Production"

from iotUserClient.popups.credentials import Credentials
from ConfigParser import *

devices = []
credentials = None
config = ConfigParser()
ioMap = None
pinTypes = ''
usedRelays = 0
usedOutputs = 0
appConfigFileName = 'app.config'


def loadSettings():
    global credentials, devices
    credentials = Credentials()
    if config.read(appConfigFileName):
        if config.has_option('general', 'username'):
            credentials.userName = config.get('general', 'username')
        if config.has_option('general', 'password'):
            credentials.password = config.get('general', 'password')
        if config.has_option('general', 'server'):
            credentials.server = config.get('general', 'server')
        if config.has_option('general', 'broker'):
            credentials.broker = config.get('general', 'broker')
        if config.has_option('general', 'devices'):
            devicesStr = config.get('general', 'devices')
            devices = [x.strip() for x in devicesStr.split(';')] if devicesStr else []

def saveSettings():
    if not config.has_section('general'):
        config.add_section('general')
    config.set('general', 'username', credentials.userName)
    config.set('general', 'password', credentials.password)
    config.set('general', 'server', credentials.server)
    config.set('general', 'broker', credentials.broker)
    config.set('general', 'devices', ';'.join(devices))
    with open(appConfigFileName, 'w') as f:
        config.write(f)