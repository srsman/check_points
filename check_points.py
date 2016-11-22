import os
from selenium import webdriver
import time
from twilio.rest import TwilioRestClient 


chromedriver = "chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://182.92.48.186/sac/login/login_lb.htm")

# time.sleep(3)

elem = driver.find_element_by_xpath("//tr[2]/td[4]")
print("start==========================")
print(elem.text)

while (elem.text != "点击访问"):
	nowStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	print("["+nowStr+"] "+"成绩没有出来")
	driver.refresh()
	elem = driver.find_element_by_xpath("//tr[2]/td[4]")
	time.sleep(60)
	
nowStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("["+nowStr+"] "+"成绩出来了")
print(elem.text)

# put your own credentials here 
ACCOUNT_SID = "ACxxxxxxxxxxxxxxxx" 
AUTH_TOKEN = "a9exxxxxxxxxxxxxxxxx" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
	to="+8613666666666", 
	from_="+1666666666", 
	body="成绩出来了",  
) 

driver.quit()