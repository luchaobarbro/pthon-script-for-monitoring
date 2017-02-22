import psutil

def infoCollect():
    pidList = psutil.pids()
    for pid in pidList:
        ps = psutil.Process(pid)
        print(ps.name())
        print(ps.status())
        print(ps.memory_percent())

infoCollect()