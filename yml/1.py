from class_changerate1 import DB
from get_config import get_config
data, tables = get_config()
data.update({'table':"tabla1"})
obj = DB(host = data["host"], user = data["user"], passwd = data["password"], database = data["database"], table = data["table"])
obj.create_table()
obj.set_data_generation()
#end = datetime.now().replace(microsecond=0)
#print "Execution Time (Hr:Min:Sec)", end-start
