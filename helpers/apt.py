import os
import sys
import time
#__________________________________________________________

from helpers.textFun import Tgreen, Tred, Tyellow
from pprint import pprint
#__________________________________________________________



def apt_update():
    # update system
    Tyellow(' system update ')
    time.sleep(1)
    updateSystemStatus = os.system('apt update -y')

    if updateSystemStatus == 0:
        Tgreen('system updated successful')
    else:
        Tred('system updated Failed !!!')
        sys.exit()


def apt_install(package):
    Tyellow("install "+ package)
    time.sleep(1)
    install_status = os.system('apt install '+package+' -y')
    if install_status == 0:
        Tgreen(package+' install successful')
    else:
        Tred(package+' install Failed !!!')
        sys.exit()