list1 = [
    {
        "key1": "value1",
        "key2": {"key21": "value21",
                 "key22": {
                     "key221": "value221",
                     "key222": None
                 },
                 "key23": None
                 }
    }
]

for x in list1:
    for key, value in x.items():
        print(key,value)



