# Script Name   : create_dir_if_not_exist.py
# Author        : Gan Dawei
# Created       : 2019.6.5
# Version       : 1.0
# Description   : Checks to see if a directory exists in the users home directory, if not then create it

import os

file='xxx.html'
home = os.path.expanduser('~')
print(home)
try:
    if not os.path.exists(os.path.join(home,file)):
        os.makedirs(os.path.join(home,file))
        print('already create file')
    else:
        print('file already exist')
except Exception as e:
    print(e)



