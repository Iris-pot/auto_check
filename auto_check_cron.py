#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
# Author  : zhaimingyang
# Time    : 2020/9/12 22:52
# Memo    : 西财自动打卡脚本-定时执行任务版本
"""
import logging
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from apscheduler.schedulers.blocking import BlockingScheduler


def log_set():
    """
    日志设置
    :return:
    """
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        filename='auto.log',
        level=logging.INFO,
        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    return logger


def check_data(logger, data):
    """
    参数校验
    :param logger:
    :param data:
    :return:
    """
    keys_list = ['username', 'password', 'prov', 'city', 'region', 'addr']
    if set(data.keys()) != set(keys_list):
        raise Exception('参数不全：请补充账号、密码、省、市、区、地址参数！')
        
    for key in data.keys():
        if data[key]:
            logger.info('{}参数输入成功'.format(key))
        else:
            raise Exception('参数不能为空：请补充账号、密码、省、市、区、地址信息！')


def log_in(logger, driver, data):
    """
    登录
    :param driver:
    :param data:
    :return:
    """
    # 账号登陆
    log_in_url = 'https://authserver.swufe.edu.cn/authserver/login?service=http%3a%2f%2fxsdaka.iswufe.info%2f'
    driver.get(log_in_url)
    time.sleep(2)
    
    username_elem = driver.find_element_by_id('username')
    username_elem.send_keys(data['username'])
    password_elem = driver.find_element_by_id('password')
    password_elem.send_keys(data['password'])
    driver.find_element_by_xpath('//*[@id="casLoginForm"]/p[4]/button').click()
    logger.info('点击登录按钮，成功')
    
    # 点击“每日上报”按钮
    check_in_url = 'http://xsdaka.iswufe.info/XSSB/Index'
    driver.get(check_in_url)
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[3]/img').click()
    logger.info('点击每日上报按钮，成功')


def file_table(logger, driver, data):
    """
    表单填写
    :param logger:
    :param driver:
    :param data: 用户传入的信息
    :return:
    """
    table_url = 'http://xsdaka.iswufe.info/XSSB/Main'
    driver.get(table_url)
    time.sleep(5)

    # 填写当前所在的省市区
    id_dict = {
        'DQSZDPRO': data['prov'],
        'DQSZDCITY': data['city'],
        'DQSZDREG': data['region']}
    for id in id_dict.keys():
        opts = driver.find_element_by_id(id)
        Select(opts).select_by_visible_text(id_dict[id])
    # 填写当前所在地详细地址
    driver.find_element_by_xpath('//*[@id="DQSZDXQ"]').clear()
    driver.find_element_by_xpath('//*[@id="DQSZDXQ"]').send_keys(data['addr'])
    logger.info('填写基本情况，成功')

    # 填写是或否的选项
    driver.find_element_by_xpath('//*[@id="STSFYC"]/option[2]').click()
    driver.find_element_by_xpath('//*[@id="SFBZD"]/option[3]').click()
    driver.find_element_by_xpath('//*[@id="JSSFBQZ"]/option[3]').click()
    driver.find_element_by_xpath('//*[@id="SFJCYQRY"]/option[3]').click()
    driver.find_element_by_xpath('//*[@id="SFJCFR"]/option[3]').click()
    driver.find_element_by_xpath('//*[@id="SFJCQZBR"]/option[3]').click()
    driver.find_element_by_xpath('//*[@id="SFDGYQ"]/option[3]').click()
    driver.find_element_by_xpath('//*[@id="FHCD"]/option[3]').click()
    driver.find_element_by_xpath('//*[@id="LKCD"]/option[3]').click()
    driver.find_element_by_xpath('//*[@id="SFHCDYW"]/option[3]').click()
    driver.find_element_by_xpath('//*[@id="SFGLGC"]/option[3]').click()
    logger.info('填写健康情况、接触情况、旅居情况、离返蓉情况、其他情况，成功')
    
    # 点击勾
    driver.find_element_by_xpath('//*[@id="checkb"]').click()
    # 点击提交按钮
    driver.find_element_by_xpath('//*[@id="loadingDiv"]/button').click()
    confirm = driver.switch_to.alert
    confirm.accept()


def auto_check():
    # 请输入信息，username和password是校园网的账号密码，prov、city、region、addr是填表时的省、市、区、地址信息。
    # data里为空会报错
    data = {
        'username': 'xxx',
        'password': 'xxx',
        'prov': 'xxx',
        'city': 'xxx',
        'region': 'xxx',
        'addr': 'xxx'}
    logger = log_set()
    logger.info('start')
    check_data(logger, data)
    driver = webdriver.Chrome()
    log_in(logger, driver, data)
    file_table(logger, driver, data)
    time.sleep(10)
    driver.quit()
    logger.info('end')


if __name__ == '__main__':
    """
    main
    """
    print('start')
    scheduler = BlockingScheduler()
    # scheduler.add_job(auto_check, 'interval', seconds=2, id='auto')
    # 此处指定时间执行打卡
    scheduler.add_job(auto_check, 'cron', hour='14', minute='03', id='auto')
    scheduler.start()
