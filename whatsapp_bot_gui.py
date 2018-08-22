# -*- coding: utf-8 -*-
"""
Created by Taha Khursheed
"""

import tkinter as tk           #For the GUI
import time                    #For adding delays to script
import pandas as pd            #For reading excel file
from selenium import webdriver #For controlling web whatsapp
import random as rd            #For randomizing the replies
import os

#Main tkinter -- GUI
window = tk.Tk()
window.geometry('500x500')
window.title("WhatsBot-Automate WhatsApp")

 
#Function to process what happens after clicking submit.(backend)
def click():
    cnames_input=cnames_entry.get()
    m_input=messages_entry.get()
    
    fpath=fpath_entry.get()
    print(fpath)
    print(var1.get())
    if(var1.get()==1):
        print("I am here A")
        if(fpath==""):
            print("I am here b")
            all_names=cnames_input.split(",")
            replies=m_input.split(",")
            messages=customize_messages(all_names, replies)
            send_messages(all_names,messages)
        else:
            print("I am here C")
            df=pd.read_excel(fpath, dtype={'Names':str, 'Replies':str} )
            all_names = df['Names']    
            replies = df['Replies'][0:5]
            messages=customize_messages(all_names, replies)
            send_messages(all_names,messages)
            
def customize_messages(all_names, replies):
    messages =[]
    for name in all_names:
        first_name=name.split(" ")[0]
        rd.shuffle(replies)
        messages.append(replies[0].format(first_name))
    return messages
  
def send_messages(all_names,messages):
    #driver = webdriver.Chrome()
    #driver.get('https://web.whatsapp.com/')
    
    #Send message for each contact in the list
    for i in range(len(all_names)): 
        
        #Code to Find the Whatsapp Search Box to search contacts.
        search_box=driver.find_element_by_class_name('_2cLHw') 
        #Note: WhatsApp sometimes changes the class names
        #if so,'inspect element' and find the new class name
        
        name=all_names[i]
        msg=messages[i]
        actions = webdriver.ActionChains(driver)
        actions.move_to_element(search_box)
        actions.click()
        actions.send_keys(name)
        actions.perform()
        
        
        #Sleeping for awhile so that the search result is shown
        time.sleep(1)
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()
        
        #Finding Message box to enter message
        msg_box = driver.find_element_by_class_name('_2S1VP')
        
        #Typing the message
        msg_box.send_keys(msg)
        
        #Clicking the Send button 
        button = driver.find_element_by_class_name('_35EW6')
        button.click()

#-----------MAIN--------------

#Starting the WebDriver
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')


#GUI
#Labels

tk.Label(window, text="WhatsBot: Automate WhatsApp",width=25,font=("bold", 20)).place(x=80,y=53)

#Entry and Label for the Contact Names
tk.Label(window, text="Contact Name(s)",width=20,font=("bold", 10)).place(x=80,y=150)
cnames_entry = tk.Entry(window)
cnames_entry.place(x=240,y=150)

tk.Label(window, text="Message(s)",width=20,font=("bold", 10)).place(x=68,y=200)

messages_entry = tk.Entry(window)
messages_entry.place(x=240,y=200)

tk.Label(window, text="(OR)",width=20,font=("bold", 13)).place(x=150,y=235)


tk.Label(window, text="Copy/Paste excel filepath",width=20,font=("bold", 10)).place(x=70,y=280)

fpath_entry = tk.Entry(window)
fpath_entry.place(x=240,y=280)

var1 = tk.IntVar()
check=tk.Checkbutton(window, text="I have scanned the QR code and read the instructions.",width=43,font=("bold", 10),variable=var1).place(x=68,y=340)


# Button
tk.Button(window, text='Submit', command=click, width=20,bg='green',fg='white').place(x=180,y=380)

#Main Loop
window.mainloop()