import yaml
def get_config():
    f=open('config.yaml')
    data=yaml.safe_load(f)
    #db_details = data.get('mysql')
    #db_params = {'host':db_details['host'], 
    #             'user':db_details['user'], 
    #             'passwd':db_details['password'], 
    #             'database':db_details['database']}
    tables = ["tabla%s"%i for i in range(1,11)]
    return data.get('mysql'), tables
