dict1={
    "key1": "value1",
    "key2": {
            "key21": "value21",
            "key22":
                {
                    "key221": "value221",
                    "key222": None,
                    "key223": [{"key2231":"value2231"},{"key2232": None}, {"key2233": {"keyXYZ": None, "keyABC": "abc"}}, None ]
                },
            "key23": None
            }
     }

def recursion(d):
    if isinstance(d, dict):
        for k,v in d.items():
            if isinstance(v,dict) or isinstance(v,list):
                recursion(v)
            elif v == None:
                del d[k]
    elif isinstance(d, list):
        for x in d:
            if isinstance(x,dict):
                recursion(x)
            elif x == None:
                d.remove(x)
    return d


newdict= recursion(dict1)
print newdict

# dict1={"k1":"v1", "k2":"v2"}
#
# for k,v in dict1.items():
#     if type(v)==str:
#         print "success"


