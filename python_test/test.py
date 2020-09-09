__author__ = 'zenghuan'
# print("hello world")
#
# a,b = 1,2
# print(a,b)
#
# c="aaaa"
# d="eeee"
# e = "1111{}"
# f =r"3333\n"
# print(c+d)
# print("aaa""dddd")
# print(type(a))
#
# print(e.format(c))
# print(f)

# str1 = "my age is %s"%20
# print(str1)
#
# str = "my name is %s,my age is %d"%("huanhuan",30)
# print(str)
#
# print("pi=%.2f"%3.1415)
#
# name = 'tom'
# name1 = 'jerry'
# print("two boys are {} and {}".format(name, name1))
# print("{0} is first,{1} is second".format(name, name1))


# f = open("test.txt",'r')
# # line = f.read()
# lines = f.readlines()
# # print(line)
# print(lines)
# f.close()

import requests
import pytest
import yaml

# with open("test.txt",'r') as f:
#     # print(f.readlines())
#     while True:
#         line =  f.readline()
#         if line:
#             print(line)
#         else:
#             break

# fp  = requests.get("http://www.baidu.com")
# print(fp.status_code)
# print(fp.encoding)
# print(fp.text)
# # fp.encoding = "utf-8"
# # print(fp.encoding)
# print(type(fp.text))





# fp_post = requests.post("http://httpbin.org/post",data={"name":"zuche"})
# print(fp_post.status_code)
# print(fp_post.text)
# print(type(fp_post.json()))
# text_json = fp_post.json()
#
# print(text_json)
# print(text_json['origin'])

ya = yaml.load(open("config.yaml"))
yb = """
 - name
 - age
 - gender
 - a: 1

"""
print(ya)
print(type(ya))
print(ya['EMAIL']['Smtp_Sender'])

print(yaml.load(yb))
print(type(yaml.load(yb)))

yc = ['name', 'age', 'gender', {'a': 1}]
print(yaml.dump(yc))
print(yaml.dump({'EMAIL': {'Smtp_Sender': 'test@tenez.com', 'Smtp_Server': 'smtp.mxhichina.com'}}))


















