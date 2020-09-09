__author__ = 'zenghuan'

import json
info = [{"name":"tom","age":23},{"name":"Jack","age":30}]

# print(type(info))
# print(info[0]["name"])
# data = json.dumps(info,indent=4)
# print(data)
# print(type(data))
# json.dump(info,open("json_dump.json","w"))

#loads 将字符串转换为json
# str = '''[{"name":"huanhuan","age":20},{"name":"xixi","age":1}]'''
#
# print(type(str))
# data = json.loads(str)
# print(type(data))
# print(data)


data2 = json.load(open("json_dump.json","r"))
print(data2)
print(type(data2))
print(data2[0]["age"])