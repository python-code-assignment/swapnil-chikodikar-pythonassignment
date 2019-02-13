dict1 = {
    "key1": "value1",
    "key2": {
            "key21": "value21",
            "key22":
                {
                    "key221": "value221",
                    "key222": None,
                    "key223": [{"key2231": "value2231"}, {"key2232": None}]
                },
            "key23": None
            }
     }


def recursion(d):
    for k, v in d.items():
        if isinstance(v, dict):
            recursion(v)
        elif v is None:
            del d[k]
    return d


newdict = recursion(dict1)
print newdict