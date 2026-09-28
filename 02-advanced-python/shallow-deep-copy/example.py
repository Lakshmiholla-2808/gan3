import copy
base = {"db": {"host": "localhost"}, "debug": True}
shallow = copy.copy(base)
deep = copy.deepcopy(base)
shallow["db"]["host"] = "prod"
print(base["db"]["host"], deep["db"]["host"])
