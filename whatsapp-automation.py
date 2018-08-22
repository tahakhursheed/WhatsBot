# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:44:04 2018

@author: tahak
"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
flag= True

while(flag) :
    name = input('Enter the name of user or group : ')
    msg = input('Enter your message : ')
    count = int(input('Enter the count : '))

    input('Enter anything after scanning QR code')

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_2S1VP')

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_35EW6')
        button.click()
        
    tempinput=input("Continue?")
    flag=bool(tempinput)
