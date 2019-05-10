import os
from time import sleep
from threading import Thread
from datetime import datetime

start = datetime.now().replace(microsecond=0)

def execute(file):
    os.system("python %s.py"%file)
def writedata():
    threads = []
    for i in range(1,11):
        t=Thread(target=execute,args=(i,))
        t.start()
        threads.append(t)
    print("waiting to data insert")
    for thr in threads:
        while True:
           if not thr.isAlive():
               break
           else:
               sleep(10)
    #print("cleaning started")
    t=Thread(target=execute,args=("remove_data",))
    t.start()
    

if __name__ == "__main__":
    writedata()

end = datetime.now().replace(microsecond=0)
print "Execution Time (Hr:Min:Sec)", end-start

