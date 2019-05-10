"""
Connect to the Windows and Linux VM
    ##############################
    Install pywinrm on Windows machine
    check::
    Pre requisite steps to run on windows machine
    run as administrator
    winrm quickconfig
    winrm e winrm/config/listener
    winrm set winrm/config/service '@{AllowUnencrypted="true"}'
"""
#from lib import logger
#from lib.WINRM import WINRM
from multiprocessing import Process
import winrm
import os
import paramiko

class Win(object):
    def __init__(self):
        """
            init() method of ConnWinCls
        """
        self.winrmclient = None
    
    def connect(self, host_ip, usr, pwd):
        """
        - **parameters**, **types**, **return** and **return types**::
            :param os_type : windows/linux
            :param host_ip: ip address of the Windows host
            :param usr: username of the Windows Host
            :param pwd: Password of the Windows Host
            :type os_type: string
            :type host_ip: string
            :type u_name: string
            :type pwd: string
        """
        self.os_type = 'windows'
        self.host_ip = host_ip
        self.usr = usr
        self.pwd = pwd
        try:
            #import pdb;pdb.set_trace()
            self.winrmclient = winrm.Session(host_ip, auth=(usr, pwd))
        except Exception as e:
            print ('connection failed')
            raise Exception(str(e))


    def run(self, cmd):
        resp = self.winrmclient.run_cmd(cmd)
        
        #import pdb;pdb.set_trace()
        #cur = os.getcwd()
        #print "++++++++++++++++++++",cur
        #os.chdir("C:\data gen")
        #next_dr= os.getcwd()
        #print "____________________",next_dr
        stdout,stderr = None, None
        statuscode = resp.status_code
        if statuscode==0:
            stdout = resp.std_out
        else:
            stderr = resp.std_error
        print(stdout, stderr) 
        return stdout

    def lin_connect(self, *lin):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=lin[0], username=lin[1], password=lin[2])
	#print lin[0],lin[1],lin[2]
        stdin, stdout, stderr = ssh.exec_command('python /root/ravi/data.py')
	print stdout.readlines()
        #aa=stdout.read()
 
def start_thread(hosts,lin_host):
        """
        @summary: Start Data generation on all tables in database using threading.
        """
        connections=[]
        try:
           process = []
           for host in hosts:
               host_instance = Win()
               host_instance.connect(*host)
               connections.append(host_instance)
               process.append(Process(target=host_instance.run, args=("python C:\\datagen\\File-server-code-data-Changerate.py",)))
           for lin in lin_host:
               #self.lin_connect(lin)
               obj = Win()
               process.append(Process(target=obj.lin_connect, args=lin))
           for i in process:
               i.start()
               print "connection created"
           for i in process:
               i.join()
#           for con in connections:
#               con.on_disconnect()
        except Exception as err:
           raise Exception(err)
           print "Error: ############# Unable to start thread ################"


#w = Win()
hosts = [("192.168.122.%s"%x, "administrator","Sungard01") for x in range(101,103)]
lin_host = [("192.168.122.%s"%x, "root","Sungard01") for x in range(10,12)]
#w.connect("192.168.122.101","administrator","Sungard01")
#print(w.run("python C:\\datagen\\File-server-code-data-Changerate.py"))

start_thread(hosts, lin_host)
