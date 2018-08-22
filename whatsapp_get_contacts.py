# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 20:59:31 2018

@author: tahak
"""
import os
#import sys
import time
import pandas as pd
from selenium import webdriver
import random as rd
#from selenium.webdriver.chrome.options import Options

#from selenium.webdriver.common.by import By

#chrome_options = Options()
#chrome_options.add_argument("user-data-dir=" + os.path.dirname(sys.argv[0]))
#driver = webdriver.Chrome(chrome_options=chrome_options)

def read_excel(fname, fpath):
    os.path.join(fpath, fname)
    
    df=pd.read_excel(fname, dtype={'Names':str, 'Replies':str} )
    
    all_names = df['Names']    
    replies = df['Replies'][0:5]
    first_names= []
    messages =[]
    for name in all_names:
        first_name=name.split(" ")[0]
        first_names.append(first_name) 
        rd.shuffle(replies)
        messages.append(replies[0].format(first_name))
    return all_names, messages


driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
#search_box=driver.find_element_by_class_name('jN-F5 copyable-text selectable-text')
all_names, messages = read_excel('names_and_replies.xlsx','C:\\Users\tahak\OneDrive\Pet Projects');
input('Enter anything after scanning QR code')

for i in range(len(all_names)): 
#Find the Search Box to search contacts.
    search_box=driver.find_element_by_class_name('_2cLHw')
    name=all_names[i]
    msg=messages[i]
    actions = webdriver.ActionChains(driver)
    actions.move_to_element(search_box)
    actions.click()
    actions.send_keys(name)
    actions.perform()
    
    
    #Sleeping for awhile (not necessary) Clicking on the user from search results.
    time.sleep(1)
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    
    #Message box found
    msg_box = driver.find_element_by_class_name('_2S1VP')
    
    #Tyoe the message
    msg_box.send_keys(msg)
    #Send button click
    button = driver.find_element_by_class_name('_35EW6')
    button.click()
    
#tempinput=input("Continue?")
#flag=bool(tempinput)

