from class_changerate1 import DB
from get_config import get_config
data, tables = get_config()
data.update({'table':"tabla1"})
#table = "tabla1"
#db_params = {'host':"192.168.122.48", 'user':"root", 'passwd':"Sungard01!", 'database':"sla", 'table':tableobj = DB(**db_params)
obj = DB(host = data["host"], user = data["user"], passwd = data["password"], database = data["database"], table = data["table"])
obj.delete_data_generated()

