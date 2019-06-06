# Script Name   : show_me_code.py
# Author        : Gan Dawei
# Created       : 2019.6.6
# Version       : 1.0
# Description   : build code for something or anything need register.


import random
import string

def str_code(num,length):
    file = open('code.txt', 'wb')
    for i in range(num):

        char = string.ascii_letters+string.digits

        code = [random.choice(char) for i in range(length)]

        code = ''.join(code)+'\n'

        file.write(code.encode('utf-8'))
    file.close()

    print('Code build already finish!')

if __name__=='__main__':
    str_code(200,10)