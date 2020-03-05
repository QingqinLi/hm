# 配置文件

lst = __file__.split('/')
print(lst)
base_path = "/".join(lst[0:-2])
userinfo = '/'.join([base_path, 'db', 'userinfo'])
print(userinfo)

