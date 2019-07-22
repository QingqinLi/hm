import sys
import os
# base_path = "/".join(__file__.split("/")[:-2])
# print(base_path)
# sys.path.append(base_path)

# # from core import main
# from core import student

base_path = "/Users/qing.li/PycharmProjects/hm"
name = 'old_boy'
print(os.sep.join([base_path, name]))
if os.name == 'nt':
    print('\\'.join([base_path, name]))
else:
    print("/".join([base_path, name]))

# # from core import main
# from core import student


