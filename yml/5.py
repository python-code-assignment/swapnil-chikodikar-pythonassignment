from class_changerate1 import DB
from get_config import get_config
data, tables = get_config()
data.update({'table':"tabla5"})
#table = "tabla5"
#db_params = {'host':"192.168.122.48", 'user':"root", 'passwd':"Sungard01!", 'database':"app1", 'table':table}
obj = DB(host = data["host"], user = data["user"], passwd = data["password"], database = data["database"], table = data["table"])
obj.set_data_generation()
#end = datetime.now().replace(microsecond=0)
#print "Execution Time (Hr:Min:Sec)", end-start

