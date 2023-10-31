from __future__ import print_function
import os
from collections import OrderedDict
from datetime import datetime
import json


def uptime():
    ''' Return the information about up system in /proc/uptime
    as a dictionary '''
    up_time = OrderedDict()
    with open('/proc/uptime') as f:
        for line in f:
            up_time = line
    return up_time


def load_stat():
    ''' Return the information about load system in /proc/loadavg
    as a dictionary '''
    loadavg = {}
    f = open("/proc/loadavg")
    con = f.read().split()
    f.close()
    loadavg['lavg_1'] = con[0]
    loadavg['lavg_5'] = con[1]
    loadavg['lavg_15'] = con[2]
    loadavg['nr'] = con[3]
    loadavg['last_pid'] = con[4]
    return loadavg


def meminfo():
    ''' Return the information in /proc/meminfo
    as a dictionary '''
    mem_info = OrderedDict()
    with open('/proc/meminfo') as f:
        for line in f:
            mem_info[line.split(':')[0]] = line.split(':')[1].strip()
    return mem_info


def version():
    ''' Return the information in /proc/version
    as a dictionary '''
    ver = OrderedDict()

    with open('/proc/version') as f:
        for line in f:
            ver = line
    return ver


current_DateTime = datetime.now()
data = {'log_system': []}
data['log_system'].append({
    'timestamp': int(datetime.timestamp(current_DateTime)),
    'uptime': uptime(),
    'loadavg': load_stat(),
    'version_OS': version(),
    'Total_memory': meminfo()['MemTotal'],
    'Free_memory': meminfo()['MemFree']
})

log_file_name = f'{datetime.today().strftime("%Y-%m-%d")}' + '-awesome-monitoring.log'
base_path = '/var/log'
full_path = os.path.join(base_path, log_file_name)

if os.path.isdir(base_path):
    with open(full_path, 'a+', encoding='utf-8') as file:
        json.dump(data, file)
        file.write('\n')
else:
    print('No directory or permission denied for this directory')


