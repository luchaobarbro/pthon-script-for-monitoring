# This script collects windows process information using module psutil

import psutil

def infoCollect():
#   collect all PID using method pids() in module psutil
    pidList = psutil.pids()
    
#   get corresponding process information with Process object
#   using PID to create Process object    
    for pid in pidList:
        ps = psutil.Process(pid)
        print(ps.name())
        print(ps.status())
        print(ps.memory_percent())

infoCollect()
