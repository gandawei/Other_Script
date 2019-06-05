# Script Name   : input_date_calc_days.py
# Author        : Gan Dawei
# Created       : 2019.6.5
# Version       : 1.0
# Description   : After input date calculate days from begining day

import datetime

def calc_days():
    year = input('Please input year:')
    month = input('Please input month:')
    day = input('Please input day:')
    date1 = datetime.date(year=int(year),month=int(month),day=int(day))
    date2 = datetime.date(year=int(year),month=1,day=1)
    return((date1-date2).days+1)

if __name__=='__main__':
    print('这一天是这一年的第{}天'.format(calc_days()))