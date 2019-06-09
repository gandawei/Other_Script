from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from data_mango_save_fordemo import mango_save

import time
import sys,io
import re


sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
username='123777'
Password ='123456'
def wait_time_id(driver,time,id):
    set_time = int(time)
    id = str(id)
    try:
        WebDriverWait(driver, set_time).until(EC.presence_of_element_located(By.ID,id))
    except Exception as e:
        print('Wait id {} too long'.format(id))
        pass
def wait_time_CLASS(driver,time,className):
    set_time = int(time)
    className = str(className)
    try:
        WebDriverWait(driver, set_time).until(EC.presence_of_element_located(By.CLASS_NAME,className))
    except Exception as e:
        print('Wait class {} too long'.format(className))
        pass
def login_Pass(driver, url):
    driver.get(url)
    wait_time_id(driver, 30, 'txtUserName2')
    account = driver.find_element_by_xpath('//input[@name="txtUserName2"]')
    account.clear()
    account.send_keys(username)
    password = driver.find_element_by_xpath('//input[@name="txtPassword2"]')
    password.clear()
    password.send_keys(Password)
    password.send_keys(Keys.RETURN)
    print('登陆完成')
    time.sleep(5)
    if password == "123456":
        driver.find_element_by_xpath('//input[@value="下次再说"]').click()
        time.sleep(2)
    return driver
def open_except_package(table,driver,data):
    data=data
    driver_new=driver
    table = table
    driver_new.get(data['url'])
    time.sleep(10)
    html = driver_new.page_source
    pattern = '<span data-localize="sty_lbl_hours">学时</span>：</span>(.*?)<span data-localize="kng_lbl_minutes">(.*?)</span> <span class="text-grey ml30"><span data-localize="kng_lbl_leancount">'
    time1 = re.findall(pattern, html)[0]
    print('需要等待{}分钟'.format(time1))#测试用 可删除
    if str(time1[1]) == "分钟":
        total_time = 60 * (float(time1[0]) + 0.1)
    else:
        total_time = int(time1[0]) + 20
    time.sleep(total_time)
    condition = {'_id': data['_id']}
    set = {'$set': {'code': 300}}  # 300代表已完成
    table.update_data(condition, set)
    print('Tag外处理子程序已完成')

def open_package(table,driver,data):
    data=data
    url=data['url']
    driver_new = driver
    table=table
    if url is not None:
        refresh_times = []
        driver_new.get(url)
        wait_time_id(driver_new, 15, 'btnStartStudy')
        content = driver_new.page_source.encode()
        pattern = '<td class="fontnumber">(.*?)</td>'
        process_list = re.findall(pattern, str(content))
        for j in process_list:
            value = j.replace('\\n', '').replace(' ', '').replace('\\xc2\\xa0', '')
            if value != '100.0%':
                refresh_times.append(value)
        for j in range(len(refresh_times)):
            wait_time_id(driver_new, 10, 'fontnumber')
            driver_new.find_element_by_xpath("//input[@type='submit']").click()
            wait_time_CLASS(driver_new, 10, 'text-grey')
            html = driver_new.page_source
            pattern = '<span data-localize="sty_lbl_hours">学时</span>：</span>(.*?)<span data-localize="kng_lbl_minutes">(.*?)</span> <span class="text-grey ml30"><span data-localize="kng_lbl_leancount">'
            time1 = re.findall(pattern, html)[0]
            if str(time1[1]) == "分钟":
                total_time = 2 * (float(time1[0]) + 0.2)  # 测试
            else:
                total_time = int(time1[0]) + 20
            time.sleep(total_time)
            driver_new.get(url)
    condition = {'_id': data['_id']}
    set = {'$set': {'code': 300}}  # 300代表已完成
    table.update_data(condition, set)
    print('Tag处理子程序已完成')

def url_from_db_open(driver):
    driver_new=driver
    condition={'code':200,'name':username}
    result={'url':1,'tag':1,'_id':1}
    table=mango_save()
    list=table.find_url(condition,result)
    for i in list:
        if i['tag'] not in ['CoursePackage']:
            open_except_package(table,driver_new,i)
            print('执行调用Tag标签外的程序')
        else:
            open_package(table,driver_new,i)
            print('执行调用处理Tag标签的程序')
    time.sleep(1) #测试用 后期可删除

if __name__ == "__main__":
    detail_url_list = []
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    #driver = webdriver.Chrome('./chromedriver.exe')
    login_url = 'http://bajuintl.yunxuetang.cn'
    driver_new = login_Pass(driver, login_url)
    url_from_db_open(driver_new)


