# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 21:50:58 2020

@author: samarth
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://accounts.xyz.com/login")

assert "XYZ" in driver.title             #this allows  to verify specifc keyword on a login page to verify if the url is rightly reached 

username = driver.find_element_by_id("Email")
username.clear()
username.send_keys("abc@gmail.com")

password = driver.find_element_by_name("Password")
password.clear()
password.send_keys("pwd123#")

driver.find_element_by_name("LOGIN").click()
