import mysql.connector
import psycopg2
from faker import Faker
from multiprocessing import Process
from datetime import datetime
import paramiko
import re
import time
fake=Faker()

from get_config import get_config
data, tables = get_config()

start = datetime.now().replace(microsecond=0)

class DB:
    def __init__(self,host,user,passwd,database,table,port="3306"):
       self.conn = mysql.connector.connect ( host=host, user=user, passwd=passwd, port=port, database=database, use_pure=True)
       self.cur = self.conn.cursor(buffered=True)
       self.table = table
       self.lis = [890]
       self.tb = [1.4,2.1,2.8]
    
    def on_disconnect(self):
        # code that runs after the connection has already closed
        # (to finalize the service, if needed)
        self.conn.close()
        print("Disconnected")
    
    def set_data_generation(self,input_range=data["input_range"]):
        print "Connection created"
        for i in xrange(1,input_range):
            name=fake.name()
            phone=fake.random_int()
            address=fake.country()
            street=fake.state()
            comment=fake.text()
            sub1=fake.text()
            sub2=fake.text()
            sub3=fake.text()
            sub4=fake.text()
            sub5=fake.text()
            sub6=fake.text()
            sub7=fake.text()
            sub8=fake.text()
            sub9=fake.text()
            sub10=fake.text()
            description=fake.text()
            val=(i,name,phone,address,street,comment,sub1,sub2,sub3,sub4,sub5,sub6,sub7,sub8,sub9,sub10,description)
            data = [val for x in xrange(100)]
            query =  """ INSERT INTO {} (ID,NAME,PHONE,ADDRESS,STREET,COMMENT,SUB1,SUB2,SUB3,SUB4,SUB5,SUB6,SUB7,SUB8,SUB9,SUB10,DESCRIPTION) \
                   VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""".format(self.table)
            self.cur=self.conn.cursor(prepared=True)
            self.cur.executemany(query, data)
            self.conn.commit()
            if self.table == "tabla1":
                if i%200 == 0:
                    self.delete_data_generated()
        print "Records created successfully";
        self.conn.close()

    
    def delete_data_generated(self):
        """
        @summary: Delete some amount of Data generated on Mysql database,
                  To achieve data changerate.
        """

	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname='192.168.122.48', username='root', password='Sungard01')

	stdin, stdout, stderr = ssh.exec_command('du -sh /var/lib/mysql/')
        aa=stdout.read()
        #print type(aa), aa
        #aap = aa[:4]
        #bap = re.findall('[-+]?\d*\.\d+|\d+',aa)
        sap = re.findall('[-+]?\d*\.\d+|\d+',aa)
        #import pdb;pdb.set_trace() 
        #print sap
        #del = re.split('M |, ',sap)
        data = float(sap[0])
        #lis = [700,900]
        #tb = [1.4,2.1,2.8]
        #import pdb;pdb.set_trace()
        if "T" in aa and self.tb:
            if data >= self.tb[0]:
                #for i in self.tb:
                print "Database Limit reached {} TB Delete operation is Activated".format(self.tb[0])
                query4 = "drop table %s"%self.table
                self.cur.execute(query4)
                self.conn.commit()
                self.tb.pop(0)
                time.sleep(10)
                self.create_table() 
            else:
                print "######### Data Limit is < {} TB ############".format(self.tb[0])
        if "G" in aa and self.lis:
            #import pdb;pdb.set_trace()
            if data >= self.lis[0]:
                #for j in lis:
                print "Database Limit reached {} GB Delete operation is Activated".format(self.lis[0])
                query1 = "drop table %s"%self.table
                self.cur.execute(query1)
                self.conn.commit()
                self.lis.pop(0)
                time.sleep(10)
                self.create_table()
            else:
                print "######### Data Limit is < {} GB ############".format(self.lis[0])

    def optimize(self,tables):
        for i in tables:
            print i, "Optimized"
            query3 = "OPTIMIZE TABLE {}".format(i)
            self.cur.execute(query3)
            #time.sleep(50)

    def create_table(self):
        query2 = "set global max_prepared_stmt_count=9000000223344556677"
        query3 = "set global general_log = 'ON'"
        self.cur.execute(query2)
        self.cur.execute(query3)

        query = "SHOW TABLES LIKE '{}'".format(self.table)
        self.cur.execute(query)
        val= self.cur.fetchall()
        print type(val), val
        if val:
            print "Table exists"
        else:
            self.cur.execute("""CREATE TABLE {}
            (ID INT(100) NOT NULL,
            NAME VARCHAR(255) NOT NULL,
            PHONE INT(100) NOT NULL,
            ADDRESS VARCHAR(255) NOT NULL,
            STREET  VARCHAR(255) NOT NULL,
            COMMENT VARCHAR(255) NOT NULL,
            SUB1 VARCHAR(255) NOT NULL,
            SUB2 VARCHAR(255) NOT NULL,
            SUB3 VARCHAR(255) NOT NULL,
            SUB4 VARCHAR(255) NOT NULL,
            SUB5 VARCHAR(255) NOT NULL,
            SUB6 VARCHAR(255) NOT NULL,
            SUB7 VARCHAR(255) NOT NULL,
            SUB8 VARCHAR(255) NOT NULL,
            SUB9 VARCHAR(255) NOT NULL,
            SUB10 VARCHAR(255) NOT NULL,
            DESCRIPTION VARCHAR(255) NOT NULL)""".format(self.table))
            print("tabla1 created")


